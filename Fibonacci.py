try:
    n = int(input('Fibonacci Number Range: '))
    s, a, b = 0, 0, 1
    if n == 0:
        print('Not Possible!')
    elif n == 1:
        print(s)
    elif n > 1:
        while s <= n:
            print(s, end=' ')
            a = b
            b = s
            s = a + b
    else:
        print('Invalid')

except ValueError:
    print('Invalid Value!')
