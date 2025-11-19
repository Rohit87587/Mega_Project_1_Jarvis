import random

n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess a number between 1 and 100: "))
    if (a < n):
        print("lower number Please!")
        guesses += 1
    elif (a > n):
        print("higher number Please!") 
        guesses += 1

print(f"Congratulations! You've guessed the number {n} in {guesses} attempts.")