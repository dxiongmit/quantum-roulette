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

# Design phi: this can be changed
circuit.h(q[0])
circuit.t(q[0])
circuit.h(q[0])

# curQ is an int that is keeps track of which players qubit to modify 
# and is 0 if it's player 1's turn to send the state 2 if it's player 2's turn.
curQ = 0
nxtQ = 2

def userTransform():
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    print("Apply an H transformation? [y/n]")
    
    app = False
    while True:
        choice = input().lower()
        if choice in valid:
            app = valid[choice]
            break
        else:
            print("[y/n]")

    if(app):
        print("Applied");
        circuit.h(q[curQ]);
        circuit.h(q[curQ]);

# addTeleport adds a new teleportation to the circuit
def addTeleport():
    global curQ
    global nxtQ
    # Design beta_00
    circuit.h(q[1])
    circuit.cx(q[1], q[nxtQ])

    # Teleportation
    circuit.cx(q[curQ], q[1])
    circuit.h(q[curQ])
    circuit.cx(q[1], q[nxtQ])
    circuit.cz(q[curQ], q[nxtQ])

    # Reset the first two qubits to the 0 state
    circuit.h(q[curQ])
    circuit.h(q[1])

    curQ, nxtQ = nxtQ, curQ

# endgame ends the game, does measurements, and draws the circuit.
def endgame():
    circuit.measure(range(0,3), range(0,3))

    # Execute the circuit on the qasm simulator or device
    job = execute(circuit, backend=simulator, shots=1000)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(circuit)
    print("\nTotal count for 00 and 11 are:",counts)

    # Draw the circuit in Console separately!!!
    circuit.draw(output='mpl')
    plot_histogram(counts)
