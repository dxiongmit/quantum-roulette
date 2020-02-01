# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:14:27 2020

@author: Hantoa

Quantum Teleportation from https://qiskit.org/textbook/ch-algorithms/teleportation.html
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

# curQ is an int that is keeps track of which players qubit to modify 
# and is 0 if it's player 1's turn to send the state 2 if it's player 2's turn.
curQ = 0
nxtQ = 2

def getUserInput():
    valid = "xyzht"
    print("Enter transformations to apply from (x,y,z,h,t)")
    
    check = True
    input_str = ""
    while True:
        choice = input().lower()
        for c in choice:
          if c not in valid:
            check = False
            break

        if check:
            input_str = choice
            break
        else:
            print("Enter a valid transformation")
    return input_str 

def player_operation(input_string, q, circuit, dagger):
    apply_gate = {
                    'x': circuit.x,
                    'y': circuit.y,
                    'z': circuit.z,
                    'h': circuit.h,                    
                    't': circuit.t,                    
    }
    if dagger: apply_gate['t'] = circuit.tdg
    
    if dagger:
        [apply_gate[gate](q) for gate in input_string]
    else:
        [apply_gate[gate](q) for gate in input_string[::-1]]

# addTeleport adds a new teleportation to the circuit
def addTeleport():
    global curQ
    global nxtQ
    
    # Design phi
    player_operation(getUserInput(), curQ, circuit, dagger=False)
    circuit.barrier()
    
    # Design beta_00
    circuit.h(1)
    circuit.cx(1, nxtQ)
    circuit.barrier()
    
    # First measurement on sender information
    circuit.cx(curQ, 1)
    circuit.h(curQ)
    #circuit.measure(curQ, curQ)
    #circuit.measure(1, 1)
    
    # After sending classical information
    circuit.cx(1, nxtQ)
    circuit.cz(curQ, nxtQ)
    circuit.barrier()
    
    curQ, nxtQ = nxtQ, curQ

# endgame ends the game, does measurements, and draws the circuit.
def endgame():
    # Apply transformation in reverse if we only care about input (currently 0?)
    #player_operation(input_string, q[2], circuit, dagger=True)
    
    # Measure q[2]
    circuit.measure(curQ, curQ)
    
    # Execute the circuit on the qasm simulator or device
    job = execute(circuit, backend=simulator, shots=1024)
    
    # Grab results from the job
    result = job.result()
    
    # Returns counts
    counts = result.get_counts(circuit)
    print("\nTotal count are:",counts)

addTeleport()
endgame()
# Draw the circuit in Console separately!!!
#circuit.draw(output='mpl')
#plot_histogram(counts)
