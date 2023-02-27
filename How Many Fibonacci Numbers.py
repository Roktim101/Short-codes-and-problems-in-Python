try:
    n = int(input('How many fibonacci numbers: '))
    s, a, b, i = 0, 0, 1, 1
    if n == 0:
        print('Not Possible!')
    elif n == 1:
        print(a)
    elif n > 1:
        for i in range(n):
            print(s, end=' ')
            a = b
            b = s
            s = a + b
    else:
        print('Invalid')

except ValueError:
    print('Invalid Value!')
