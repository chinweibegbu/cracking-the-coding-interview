def palindrome_permutation(string):
    # SPECIAL CASE: String is empty, has 1 or 2 characters
    if (len(string) < 3): return False
    
    # Count characters and number of occurences
    characters = count_characters(string)
    
    # Uncomment the line below for debugging purposes
    # print(characters)
    
    # Check if string is a permuation of a palindome
    # DETERMINANT: Must have 0 or 1 characters which occur only once and the rest of its characters must occur x times where x is a multiple of 2
    return is_palindrome(characters)

def count_characters(string):
    characters = {}
    
    for character in string:
        # Disregard spaces
        if (character == " "): continue
        
        # Change all characters to the same case
        character = character.lower()
        
        # Increment count or insert into dictionary
        if (character not in characters):
            characters[character] = 1
        else:
            characters[character] = characters[character] + 1
        
    return characters        

def is_palindrome(dict):
    # Track whether a character with only one occurence has been found
    has_odd = False
    
    # Parse the dictionary
    for count in dict.values():
        if (count %2 != 0) and (not has_odd):
            has_odd = True
        elif (count %2 != 0) and (has_odd):
            return False

    # The string is a palindrome permutation if no False was return-ed
    return True
    
print(palindrome_permutation("Tact Coa"))   # Expected: True
print(palindrome_permutation("Tact Coat"))  # Expected: False
print(palindrome_permutation("race arc"))   # Expected: True
print(palindrome_permutation("racecar"))    # Expected: True
print(palindrome_permutation(""))           # Expected: False
print(palindrome_permutation("racacar"))    # Expected: True

"""
Runtime Analysis:
    Special case checks: O(1)
    count_characters(): O(n)
    is_palindrome(): O(n)
    
    >> O(n)
    THOUGHTS: I actually made a mistake. I am meant to check if the count is odd, NOT if it is 1
"""
