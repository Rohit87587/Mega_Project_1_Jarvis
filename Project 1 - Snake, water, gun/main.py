import random
'''
1 - snake
-1 - water
0 - gun
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youdict = {"snake": 1, "water": -1, "gun": 0}
revercedict = {1: "snake", -1: "water", 0: "gun"}
you = youdict[youstr]

print(f"Computer chose: {revercedict[computer]}")
print(f"You chose: {youstr}")

if computer == you:
    print("It's a tie!")
else:
    if (you ==1 and computer == -1):
        print("You win!")
    elif (you == -1 and computer == 0):
        print("You win!")
    elif (you == 0 and computer == 1):
        print("You win!")
    elif (computer ==1 and you == -1):
        print("Computer wins!")
    elif (computer == -1 and you == 0):
        print("Computer wins!")
    elif (computer == 0 and you == 1):
        print("Computer wins!")
    else:
        print("something went wrong")