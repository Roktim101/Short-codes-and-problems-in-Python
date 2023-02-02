secret_num = str(8)
guess = ''
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_num and not out_of_guesses:
    if guess_count < guess_limit:
        if guess_count == 0:
            guess = input('You have four guesses!\nEnter a number between (0-9): ')
        else:
            guess = input('Enter another number: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Out of guesses! You lose!')
else:
    print('You win!')
