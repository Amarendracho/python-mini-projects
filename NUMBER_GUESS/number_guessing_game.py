
import random

def number_guessing():
    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Correct!")
            print("you guessed it in", attempts ,"attempts")
            break

number_guessing()


# second time same logic but variable names change  
def guessing_game():

    random_num = random.randint(1,50)
    guess_count = 0

    while True:
        guessing_num = int(input("Guess a number (1-50) : "))
        guess_count += 1

        if guessing_num > random_num:
            print("Too high")
        elif guessing_num < random_num:
            print("Too low")
        else:
            print("Guessing right number congratulations 🥳")
            break

    print(f"random number is : {random_num}")
    print("guessing number is ", guessing_num)
    print("you guessed it in", guess_count, "attempts")

guessing_game()













