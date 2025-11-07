import random
"""
1 = rock
2 paper 
3 = scissors
"""

computer = random.choice([1,2,3])
user = input("Enter rockand   paperand   scissors and   any one !: ")
userdict = {"r" : 1,  "p" : 2,  "s": 3,  }
you = userdict[user]
reversedict = {1: "rock", 2: "paper", 3: "scissors"}
print("Computer choosed",  reversedict[computer],  "and you choosed",  reversedict[you])
if computer == you:
    print("It's a tie")
else:
    if (computer == 1 and you == 2 ):
        print("you win")
    elif (computer == 1 and you == 3 ):
        print("you lose")
    elif (computer == 2 and you == 1 ):
        print("you lose")
    elif (computer == 2 and you == 3 ):
        print("you win")
    elif (computer == 3 and you == 1 ):
        print("you win")
    elif (computer == 3 and you == 2 ):
        print("you losse")
    else:
        print("Invalid input")
#rock paper scissors game

# print("Play again>? (y/n)")
# play = input()
# if play == "y":
    # import os
    # os.system("python main.py")