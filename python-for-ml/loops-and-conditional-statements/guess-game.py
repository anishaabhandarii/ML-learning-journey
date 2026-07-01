import random
number = random.randint(1, 100)
user_guess = None
count  =0
while user_guess !=number:
    print("This is  where the loop starts")
    user_guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if user_guess < number:
        print("Guess higher!")
    elif user_guess > number:
        print("Guess lower!")
    else:
        print(f"Congratulations! You guessed the number in {count} attempts.")
    print("This is where the loop ends")