a = [[1,2,3], [4,5,6], [7,8,9]]

# Initialize the output matrix with zeros
output = [[0]*len(a) for x in range(3)]
print(output)
print()

# Transpose the matrix using nested for loops
for i in range(len(a)):
    for j in range(len(a[0])):
        output[j][i] = a[i][j]

print(output)

print()

a = [[1,0,0], [2,0,0], [3,0,0]]

output = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

print(output)

