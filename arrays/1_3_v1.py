# Ver. 1: Using Python in-built functions
def URLify(string, length):
    joiner = "%20"
    
    # Split string by spaces
    words = string.split()
    
    # Join the resulting array with the joiner, %20
    # return words.join(joiner) --> WRONG
    return joiner.join(words)

print(URLify("Mr John Smith    ", 13))

"""
Runtime Analysis:
    Splitting: O(n)
    Joining: O(n)
    
    >> O(n)
"""
