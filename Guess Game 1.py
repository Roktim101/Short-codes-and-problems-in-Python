num = 27

a = ''

while a != num:
    a = int(input('Guess a number between (1-99): '))
    if a < 1 or a > 99:
        print('\nOut of range!')
    elif a > num:
        print('\nTry a lower number!')
    elif a < num:
        print('\nTry a higher number!')
else:
    print('\nYou guessed it!')
