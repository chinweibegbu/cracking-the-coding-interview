def one_away(a, b):
    # Create tracking variables
    is_changed = False
    
    # Check is_changed status by comparing lengths
    if (abs(len(a)-len(b)) == 1):
        # There has been either one decrease or one increase
        is_changed = True
        
        # Check that all letters in the shorter string are in the longer string
        smaller = a if (len(a) < len(b)) else b
        larger = a if (len(a) > len(b)) else b
        for character in smaller:
            if (character not in larger):
                # There has been a replacement
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

print(one_away("pale", "ple"))      # Expected True
print(one_away("pales", "pale"))    # Expected True
print(one_away("pale", "bale"))     # Expected True
print(one_away("pale", "bake"))     # Expected False
print(one_away("pale", "pales"))    # Expected True
print(one_away("pale", "pe"))       # Expected False
print(one_away("pale", "pale"))     # Expected True
print(one_away("pale", "pee"))      # Expected False --> ERROR

"""
Runtime Analysis:
    Variable initialisation: O(1)
    if branch #1: O(n^2), where n is the length of the smaller string 
    if branch #2: O(1)
    if branch #3: O(n)
    
    >> O(n^2)
    THOUGHTS:
    - There is a bottleneck in the first branch of the if-statement
    - Is there a way to reduce the time complexity of the string comparison?
    - Noticed that the code is actually flawed (see line 49)
    - SOLUTION: Check that the smaller has the characters AND counts of the larger apart from one character
      APPROACH: Use a hash table (??)
"""
