def get_matrix (n, m,  value):
    matrix = []
    for i in range(n):
        new_line = []
        matrix.append(new_line)
        for j in range(m):
            new_line.append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)