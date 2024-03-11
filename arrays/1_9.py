def string_rotation(s1, s2):
    # Special case #1: Strings are not equal in length
    if (len(s1) != len(s2)):
        return False
    
    # Special case #2: Strings are equal
    if (s1 == s2):
        return True
    
    # Check if the first character of s1 is in s2
    # If not in s2, not a rotation --> return False
    if (s1[0] not in s2):   
        return False 
    # Else
    else:
        # Get rotation point
        fulcrum = s2.index(s1[0])
        # Check that from the end of s2 matches the beginning of s1
        beginning_s2, end_s2 = s2[0:fulcrum], s2[fulcrum:len(s2)]
        beginning_s1 = s1[0:len(s1)-fulcrum]
        # If it is not in s1, not a rotation --> return False
        if (beginning_s1 != end_s2):
            return False
        # Else
        else:
            # Check that the beginning of s2 is a substring of s1
            end_2_is_substring = isSubstring(s1, beginning_s2)
            # If it does, it is a rotation --> return True
            if (end_2_is_substring):
                return True
            # Else, it is not a rotation --> return False
            else: 
                return False

def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False

s1, s2 = "waterbottle", "erbottlewat"
s3, s4 = "lewaterbott", "erbottlewat"
s5, s6 = "water", "errrwat"
s7, s8 = "justice", "planets"

print(string_rotation(s1, s2))  # Expected: True
print(string_rotation(s3, s4))  # Expected: True
print(string_rotation(s5, s6))  # Expected: False
print(string_rotation(s7, s8))  # Expected: False

"""
Runtime Analysis: 
    Special cases: O(1)
    Finding the rotation point: O(n)
    Slicing strings: O(n)
    isSubstring(): O(n), where n is the both length of the words
    
    >> O(n)
    THOUGHTS:
    - By adding more edge cases and tests, I was able to debug problems
"""
