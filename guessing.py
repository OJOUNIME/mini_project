secret_number = 7

print("welcome to my first guessing game")
print("can you guess my favourite number between 1 to 10? (You have 3 tries)")

for attempt in range(3):
    guess = int(input("enter your guess: "))

    if guess == secret_number:
        print("you got it! thats my favourite number!")
        break
    elif guess < secret_number:
        print("Nope! Too low. Try again.")
    else:
        print("Nope! Too high. Try again.")
else:
    print(f"Game over! You ran out of tries. The number was {secret_number}.")
