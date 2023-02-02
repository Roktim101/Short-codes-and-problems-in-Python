# Output will carry only odd numbers expect numbers with 9 in them

n = int(input('Range : '))
i = 1
while i < n:
    if i >= n:
        break
    while str(i).find('9') != -1:
        i += 2
    if i <= n:
        print(i, end=" ")
    i += 2
print()