def find_special_values(matrix):
    special_values = []

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            value = matrix[i][j]
            row_max = max(matrix[i])
            col_min = min(matrix[r][j] for r in range(rows))

            if value >= row_max and value <= col_min:
                special_values.append(value)

    return special_values

# Test the function with your example matrix
matrix = [
    [7, 8, 7],
    [5, 4, 2],
    [8, 6, 7]
]

special_values = find_special_values(matrix)
print(special_values)  # Output: [5]
