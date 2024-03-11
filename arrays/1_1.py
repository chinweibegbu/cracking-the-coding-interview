def is_unique(word):
    # Initilise the character-tracking dictionar
    char_dict = {}

    for character in word:
        # If character is in dictinary, word is not all unique
        if (character in char_dict):
            return False
        # Else, add to dictionary
        else:
            char_dict[character] = 1
    
    # Word is all unique if there is no return from the for loop
    return True

print(is_unique("abcd"))
print(is_unique("abddd"))

"""
Runtime Analysis:
    dict initialisation: O(1)
    Check if in dict: O(1)
    Insertion into dict: O(1)
    for loop: O(n), n: length of word
    
    >> O(n)
"""
