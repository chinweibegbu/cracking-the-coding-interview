# Ver. 3: Using Python replace() function
def URLify(string, length):
    joiner = "%20"
    
    # Remove any space on the right-hand side of the string
    string = string.strip()
    
    # Replace the spaces with the specified joiner
    string = string.replace(" ", joiner)
    
    # Return the URLify-ed string
    return string

print(URLify("Mr John Smith    ", 13))

"""
Runtime Analysis:
    strip(): O(n)
    replace(): O(n)
    
    >> O(n)
    CONCLUSION: Same as v1. Better in terms of readability and simplicity.
"""
