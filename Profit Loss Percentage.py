i = float(input('Invest: '))
g = float(input('Gain: '))
if g > i:
    print('Profit = ', 100 * (g - i) / i, '%')
elif i > g:
    print('Loss = ', 100 * (i - g) / i, '%')
else:
    print('No loss, no profit!')