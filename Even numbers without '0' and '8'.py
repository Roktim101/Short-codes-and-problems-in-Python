# Output will carry only even numbers expect numbers with 0 and 8 in them

a = int(input('Range : '))

for i in range(a):
    if i % 2 == 0 and "0" not in str(i) and "8" not in str(i):
        print(i, end=' ')

# another way 

a = int(input('Range: '))

result = [i for i in range(a) if i % 2 == 0 and "0" not in str(i) and "8" not in str(i)]    # used a list comprehension

print(*result)    # used the unpacking operator '*' to print the list elements separated by spaces.
