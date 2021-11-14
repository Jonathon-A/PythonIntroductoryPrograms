import random
n = random.randint(1,100)

print("Guess the number between 1 and 100 inclusive")
turns = 0
while True:
    turns += 1
    guess = int(input("Guess a number: "))
    if guess == n:
        print("You guessed the number:", n)
        break
    elif guess > n:
        print("Lower")
    elif guess < n:
        print("Higher")
print("you guessed the number in", turns, "turns, well done")
