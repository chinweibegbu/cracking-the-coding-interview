# Using dictionaries instead of arrays to check zero rows and columns
def zero_matrix(matrix):
    # Parse matrix and keep track of the locations of zeros
    zero_rows, zero_columns = {}, {}
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                zero_rows[x] = 1
                zero_columns[y] = 1
    
    # Go through matrix again such that any cell which has a matching row or column will be set to zero
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (x in zero_rows.keys()) or (y in zero_columns.keys()):
                matrix[x][y] = 0
    
    return matrix

def print_matrix(matrix, is_zeroed):
    prefix = "ZEROED -" if is_zeroed else "ORIGINAL -"
    print("{} Matrix of size {} by {}:".format(prefix, len(matrix), len(matrix[0])))
    for row in matrix:
        print(row)
    print("\n")

matrix_1 = [
    [3, 1, 3],
    [4, 0, 9],
    [8, 5, 3],
    [4, 15, 2]
]

matrix_2 = [
    [3, 1, 3],
    [4, 8, 0],
    [8, 5, 3],
    [0, 7, 2]
]

print_matrix(matrix_1, False)
print_matrix(zero_matrix(matrix_1), True)

print_matrix(matrix_2, False)
print_matrix(zero_matrix(matrix_2), True)

"""
Runtime Analysis: 
    Parsing matrix: O(mn)
    Zero-ing matrix: O(mn)
        for x loop: O(m)
        for y loop: O(n)
        comparison: O(1)
    print_matrix: O(m)
    
    >> O(mn)
    CONCLUSION: Better than Ver. 1 in terms of performance. Same in terms of space complexity.
    IMPROVEMENT: 
    - I could still potentially do it all in one parse which would not change the runtime but would reduce space complexity to O(1) and reduce the actual number of operations.
"""
