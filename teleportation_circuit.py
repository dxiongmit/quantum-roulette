# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:14:27 2020

@author: hanto
"""

import numpy as np
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import(
  QuantumCircuit,
  execute,
  Aer,
  IBMQ)
from qiskit.providers.ibmq import least_busy
from qiskit.visualization import plot_histogram

# Set credentials to access backend
#IBMQ.save_account('292ebd1c42498b47d4d3c1076b3afa016395350f214fcc5d598241639624171f63a78ddde5ae15d23445c9627c7da5e8883c42d020c4cf84451dc39e36a6c6cb')
#provider = IBMQ.load_account()

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
#device = least_busy(provider.backends(simulator=False))
#real_computer = IBMQ.get_backend('something')

# Create a Quantum Circuit acting on the q register
q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(q, c)

# Design phi
circuit.h(q[0])
circuit.t(q[0])
circuit.h(q[0])

# Design beta_00
circuit.h(q[1])
circuit.cx(q[1], q[2])

# First measurement on sender information
circuit.cx(q[0], q[1])
circuit.h(q[0])
circuit.cx(q[1], q[2])
circuit.cz(q[0], q[2])
circuit.measure(range(2,3), range(2,3))

# Execute the circuit on the qasm simulator or device
job = execute(circuit, backend=simulator, shots=100)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit in Console separately!!!
circuit.draw(output='mpl')
plot_histogram(counts)