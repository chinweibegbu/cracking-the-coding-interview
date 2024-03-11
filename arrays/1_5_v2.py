# Ver. 2: Using a hash table to count occurences
def one_away(a, b):
    # Create tracking variables
    is_changed = False
    
    # Check is_changed status by comparing lengths
    if (abs(len(a)-len(b)) == 1):
        # There has been either one decrease or one increase
        is_changed = True
        
        # Count characters and counts for both letters
        a_counter, b_counter = character_counter(a), character_counter(b)
        
        # Get longer and shorter strings
        longer, shorter = (a_counter, b_counter) if (len(a) > len(b)) else (b_counter, a_counter)
        
        # Return False is any replacements have been made
        # i.e. if char in a is not in b or if the char counts are not the same
        for key in shorter.keys():
            if ((key not in longer.keys()) or (shorter[key] != longer[key])): 
                return False
        
    elif (abs(len(a)-len(b)) > 1):
        # There has been more than one decrease or increase
        return False
    
    else:
        # Nothing changes for the is_changed variable
        # Hence, return False only if more than one replacement has been made
        is_changed = False
        
        is_replaced = False
        for i in range(len(a)):
            if (a[i] == b[i]):
                # There has been no replacement
                continue
            elif ((a[i] != b[i]) and (not is_replaced)):
                # There has been exactly one replacement 
                is_replaced = True
            elif ((a[i] != b[i]) and (is_replaced)):
                # There has been more than one replacement
                return False
    
    # There has been 0 or 1 edit made
    return True

def character_counter(string):
    counter = {}
    for character in string:
        counter[character] = 1 if (character not in counter) else (counter[character] + 1)
    return counter

print(one_away("pale", "ple"))      # Expected True
print(one_away("pales", "pale"))    # Expected True
print(one_away("pale", "bale"))     # Expected True
print(one_away("pale", "bake"))     # Expected False
print(one_away("pale", "pales"))    # Expected True
print(one_away("pale", "pe"))       # Expected False
print(one_away("pale", "pale"))     # Expected True
print(one_away("pale", "pee"))      # Expected False --> CORRECTED

"""
Runtime Analysis:
    Variable initialisation: O(1)
    character_counter(): O(n)
    if branch #1: O(n), where n is the length of the smaller string 
    if branch #2: O(1)
    if branch #3: O(n)
    
    >> O(n)
    CONCLUSION: Time complexity is better than in v1 because of the addressed bottleneck. Code is verbose.
    IMPROVEMENT: 
    - Remove the is_changed variable - checking the replacement status within the if-statement removes the need to track it elsewhere in the code
"""
