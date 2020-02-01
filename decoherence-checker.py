import random


#p is the probability of a single gate failing; n is the number of gates used so far.
def checkFail(n, p = 0.01):
        roll = random.random()
        if roll < (1 - p) ** (n + 6):
            return False
        else:
            return True
    
