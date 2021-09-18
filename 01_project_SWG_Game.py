# Snake, Water, Gun Game (SWG)

# Step 1: random module to be imported for random digit selection
import random

# Step 2: defining a function for the game rules
def SWG_Game(comp, You):
    if comp == You:
        return None
    elif comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
    elif comp == 'w':
        if You == 'g':
            return False
        elif You == 's':
            return True 
    elif comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True

# Step 3: Computer functioning of random values with the help of randint function
print("Comp Turn: Snake(s), Water(w), Gun(g)? ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

# Step 4: Input for the player's chance
You = input("Your Turn: Snake(s), Water(w), Gun(g)? ")

# Step 5: Putting Function into a variable
a = SWG_Game(comp, You)

# Step 6: F string to know what computer and player chose 
a = SWG_Game(comp, You)
print(f"Computer chose {comp}")
print(f"You chose {You}")

# Step 7: Result to be printed whether lose, win or tie
if a == None:
    print("The game is tie!")
elif a == True:
    print("You Win!")
elif a == False:
    print("You Lose!")
