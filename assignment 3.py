import random

secret_number = random.randint(1, 10)
print(f"Generated secret number: {secret_number}")

guess = int(input("Guess the number (between 1 and 10): "))
attempts = 3

import random
secret_number = random.randint(1, 10)
attempts = 3
while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    attempts -= 1
secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    attempts -= 1
else:
    print("Better luck next time!")


number = int(input("Enter the number for which you want the multiplication table: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")



def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi_result:.2f}") 
