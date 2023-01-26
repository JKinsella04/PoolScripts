# Variables
# Total shots
# Made balls
# Scratches
# Balls made off break
# Calculation
# (Made Balls + 0.5(Balls made off break) - 0.5(Scratches)) / Total shots 
# Path: qualifier.py

def calc():
    return (shotsMade + 0.5*bobs - 0.5*scratches)/totalShots

name = input("Enter the name of the player: ")


shotsMade = 0 
scratches = 0 
totalShots = 0 
bobs = 0 

playing = True
newRound = True 

roundsLeft = int(input("5 games of 9 or 3 games of 15?\n"))

while(roundsLeft):
    if(newRound):
        bobs += int(input("How many made off break?\n"))
        newRound = False

    result = int(input("Made Shot(1), Scratch(2), Nothing(3), End(9)\n"))
    
    totalShots += 1

    match result:
        case 1:
            shotsMade += 1
        case 2:
            scratches += 1
        case 3:
            print("Sad")
        case _:
            print("Current ranking: " + str(round(calc(), 3)))
            newRound = True
            roundsLeft -= 1
