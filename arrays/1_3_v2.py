# Ver. 2: Without the Python in-built functions
def URLify(string, length):
    joiner = "%20"
    
    # Create a new empty string
    result = ""
    
    # Copy the character if it is not a space and use the joiner when it is
    for i in range(0, length):
        char = string[i]
        if (char == " "):
            result += joiner
        else: 
            result += char
    
    # Return the new string
    return result

print(URLify("Mr John Smith    ", 13))

"""
Runtime Analysis:
    for loop: O(n)
        Character comparison: O(1)
        String concatenation: O(1)
    
    >> O(n)
    CONCLUSION: Performs better than v1 in that there is only one O(n) operation, unlike with v1, even though they simplify to the same value
"""
