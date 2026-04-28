# transpose of a matrix

def transpose(matrix):
    rows, cols = len(matrix),len(matrix[0])

    transposed_matrix=[[0,0,0],[0,0,0],[0,0,0]]

    for row in range(rows):
        for col in range(cols):
            transposed_matrix[col][row]=matrix[row][col]

    return transposed_matrix


matrix=input("Enter a 3x3 matrix (9 numbers separated by spaces): ")
matrix=[list(map(int, matrix.split()[i:i+3])) for i in range(0, 9, 3)]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\n")

transposed=transpose(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)

