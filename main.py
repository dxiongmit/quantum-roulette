from teleportation_circuit import *
import random
import time

#p is the probability of a single gate failing; n is the number of gates used so far.
def checkFail(n, p = 0.01):
        roll = random.random()
        if roll < (1 - p) ** n:
            return False
        else:
            return True

def startGame(p = 0.01):
    #n starts at 8, since each teleportation requires 8 gates. p is 0.01 for now.
    n = 8
    
    #curQ is the current qubit that can be chnaged, while nxtQ is the other qubit.
    curQ = 0
    nxtQ = 2
    measurable = False
    
    #score keeps track of the score
    score = [0, 0]
    while True:
        #Tells player the current fidelity; asks them whether they want to add gates.
        print("Current fidelity: " + str((1 - p) ** n))
        print("Current score: " + str(score[0]) + "-" + str(score[1]))
        
        if measurable:
            random_gate = gates[random.randint(0, extra-1)]
            print("The last player used " + str(extra) + " gates.")
            print("One of those gates was a " + random_gate + " gate.")
            print("Measure the state?")
            choice = input().lower()
            if choice[0] == 'y':
                endgame(curQ)
                break
            else: print("You did not measure the state.")
        
        measurable = True
        
        print("Add gates? [y/n]")
        choice = input().lower()
        if choice[0] == 'y':
            gates = getUserInput(curQ)
            extra = len(gates)
            n += extra
            
            player_operation(gates, curQ, circuit, False)
            
            #Giving the correct player the points
            if curQ == 0:
                score[0] += extra
            else:
                score[1] += extra
                
        else: 
            print("No gates added.")
            measurable = False
    
        print("Teleporting...")
        time.sleep(1)
        
        addTeleport(curQ, nxtQ)
        curQ = 2 - curQ
        nxtQ = 2 - nxtQ
        
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
    
    endgame(curQ)

print("Start game? [y/n]")
choice = input().lower()
if choice[0] == 'y':
    print("Enter a failure rate: leave blank for 0.01")
    choice = input()
    if len(choice) == 0:
        startGame()
    else:
        startGame(float(choice))
else:
    print("Then what are you doing?")
