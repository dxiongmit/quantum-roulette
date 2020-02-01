from teleportation_circuit import *
import random
import time

#p is the probability of a single gate failing; n is the number of gates used so far.
def checkFail(n, p = 0.01):
        roll = random.random()
        if roll < (1 - p) ** (n + 6):
            return False
        else:
            return True
        
def startGame():
    #n starts at 8, since each teleportation requires 8 gates. p is 0.01 for now.
    n = 8
    p = 0.01
    
    while True:
        #Tells player the current fidelity; asks them whether they want to add gates.
        print("Current fidelity: " + str((1 - p) ** n))
        print("Add gates? [y/n]")
        choice = input().lower()
        if choice[0] == 'y':
            gates = getUserInput()
            n += len(gates)
        
            player_operation(gates, curQ, circuit, False)
        else:
            print("No gates added.")
    
        print("Teleporting...")
        time.sleep(1)
        
        addTeleport()
        
        if checkFail(n, p):
            print("Transmission failed!")
            if curQ == 2:
                print("Player two wins!")
            else:
                print("Player one wins!")
        else:
            n += 8
    
        
    
print("Start game? [y/n]")
choice = input().lower()
if choice[0] == 'y':
    startGame()
else:
    print("Then what are you doing?")
