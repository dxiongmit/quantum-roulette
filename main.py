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

def startGame(p = 0.01):
    #n starts at 8, since each teleportation requires 8 gates. p is 0.01 for now.
    n = 8
    
    #score keeps track of the score
    score = [0, 0]
    while True:
        #Tells player the current fidelity; asks them whether they want to add gates.
        print("Current fidelity: " + str((1 - p) ** n))
        print("Current score: " + str(score[0]) + "-" + str(score[1]))
        print("Add gates? [y/n]")
        choice = input().lower()
        if choice[0] == 'y':
            gates = getUserInput()
            extra = len(gates)
            n += extra
        
            player_operation(gates, curQ, circuit, False)
            
            #Giving the correct player the points
            if extra > 5:
                if curQ == 0:
                    score[0] += 5
                else:
                    score[1] += 5
            else:
                if curQ == 0:
                    score[0] += extra
                else:
                    score[1] += extra
                
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
            break
        else:
            if score[0] >= 20:
                print("Player one wins with " + str(score[0]) + " points!")
                break
            elif score[1] >= 20:
                print("Player two wins with " + str(score[1]) + " points!")
                break
            else:
                n += 8
        
    
print("Start game? [y/n]")
choice = input().lower()
if choice[0] == 'y':
    print("Enter a failure rate: leave blank for 0.01")
    choice = input()
    if choice == None:
        startGame()
    else:
        startGame(float(choice))
else:
    print("Then what are you doing?")
