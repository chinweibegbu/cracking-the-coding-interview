def string_compression(original):
    # Special case: Empty string
    if original == "": return original
    
    compressed = ""
    
    prev = original[0]
    count = 0
    
    # Parse original string
    for i in range(len(original)):
        # Update cur
        cur = original[i]
        
        # If prev and cur are the same, increment count
        if (prev == cur):
            count += 1
        # Else, add to compressed string and reset count  
        else:
            compressed += prev + str(count)
            count = 1
        
        # If we are at the end, add to compressed string
        if (i == len(original)-1):
            compressed += prev + str(count)
        
        # Update prev and cur
        prev = cur
    
    # Return the shorter of compressed and original
    return compressed if (len(compressed) < len(original)) else original

print(string_compression("aabcccccaaa"))        # Expected: "a2b1c5a3"
print(string_compression("aabccCCCCCCccaaa"))   # Expected: "a2b1c6C1c2a3"
print(string_compression(""))                   # Expected: ""
print(string_compression("ab"))                 # Expected: "ab"

"""
Runtime Analysis: 
    O(1) for all operations except for-loop
    O(n) for for-loop, where n is the number of characters in the original string
    
    >> O(n)
    THOUGHTS:
    - I think O(n) is the Best Conceivable Time (BCR) because you have to parse the entire sting
    - If I had done a proper walkthrough before implementing, I would have caught the errors regarding:
        1. Adding prev to the compressed string rather than cur
        2. Adding the last character-count pair
    - Is there a way I could have made the cur-prev relationship more intuitive?
"""
