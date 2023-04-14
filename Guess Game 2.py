secret_num = 8
guess_limit = 4
guess_count = 0

while guess_count < guess_limit:
    guess = input(f"You have {guess_limit - guess_count} guesses!\nEnter a number between 0-9: ")
    try:
        guess = int(guess)
    except ValueError:
        print('Error! Type a integer number!')
        continue
    if guess == secret_num:
        print("You win!")
        break
    elif guess < 0 or guess > 9:
        print("Enter a number between 0-9!".upper())
        continue
    guess_count += 1
else:
    print("Out of guesses! You lose!")
    
    
