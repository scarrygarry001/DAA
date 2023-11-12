# Max No. of 1's in a matrix:
def most_ones(matrix):
    max_count = 0
    max_rows = []

    for i in range(len(matrix)):
        count = matrix[i].count(1)

        if count > max_count:
            max_count = count
            max_rows = [i]
        elif count == max_count:
            max_rows.append(i)

    return max_rows

matrix = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]
max_rows = most_ones(matrix)
print(max_rows)  

# Middle Row and Column Sum:
def middle_sum(matrix):
    n = len(matrix)
    middle = n // 2

    row_sum = sum(matrix[middle])

    col_sum = sum(matrix[i][middle] for i in range(n))

    return row_sum, col_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sum, col_sum = middle_sum(matrix)
print(row_sum, col_sum)  
