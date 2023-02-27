try:
    n = int(input('How many Fibonacci numbers: '))
    a, b = 0, 1
    if n == 0:
        print('Not possible!')
    else:
        for i in range(n):
            print(a, end=' ')
            a, b = b, a + b     # used tuple unpacking
except ValueError:
    print('Invalid value!')
