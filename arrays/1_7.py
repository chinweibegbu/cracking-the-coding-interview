def rotate_matrix(n):
    original = create_matrix(n)
    rotated = [[0 for i in range(n)] for j in range(n)]
    
    print_matrix(original, False)
    
    # Print in reordering order (bottom to top and then right)
    for y in range(n):
        for x in range(n-1, -1, -1):
            rotated[y][n-1-x] = original[x][y]
            
    print_matrix(rotated, True)

def create_matrix(n):
    matrix = [[(j*n)+i for i in range(n)] for j in range(n)]           
    return matrix

def print_matrix(matrix, is_rotated):
    prefix = "ROTATED -" if is_rotated else "ORIGINAL -"
    print("{} Matrix of size {}:".format(prefix, len(matrix)))
    for row in matrix:
        print(row)
    print("\n")

rotate_matrix(3)

"""
Runtime Analysis: 
    create_matrix: O(n^2)
    print_matrix: O(n)
    Reordering: O(n)
    
    >> O(n^2)
    THOUGHTS:
    - I had the idea down but I got stuck trying to figure out how to calculate the correct indices (i.e. the math)
    - I did not talk out loud AT ALL; I was too busy being confused
    - I should definitely do more paper coding first and the fucking walkthrough - Chinwe, do your walkthrough BEFORE you implement
    - I have noticed I find it hard to code on paper (I think a whiteboatd would be better)
    - This was horrible
        - My knee-jerk thought was "I hope I don't get a matrix question"
        - I am proud that the thought, "I should practice more matrix questions" came soon after
    - I cannot think of anyway to reduce the time complexity
    - I was so stressed implementing the bruteforce approach with another matrix, I cannot imagine doing it in place
        - That is a lie - I can imagine it
        - IDEA: Parse matrix in both directions simulatenously + Use a temp variable to switch + keep track of switched cells
"""
