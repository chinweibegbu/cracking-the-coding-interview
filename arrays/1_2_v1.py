def check_permutation(s1, s2):
    # If strings are not the same length, they are not permutations
    if (len(s1) != len(s2)): return False
    
    # If strings are the same, they are permutations 
    if (s1 == s2): return True
    
    # Count the letters and occurences of each string
    s1_letters, s2_letters = count_letters(s1), count_letters(s2)
    
    # The strings are permutations if their dictionaries are the same
    return s1_letters == s2_letters

def count_letters(string):
    letters = {}
    for char in string:
        if (char not in letters):
            letters[char] = 1
        else:
            letters[char] = letters[char] + 1
    return letters

print(check_permutation("faab", "baa"))
print(check_permutation("kla", "kla"))
print(check_permutation("ab", "ba"))

"""
Runtime Analysis:
    count_letters(n): O(n)
        dict initialisation: O(1)
        Check if in dict: O(1)
        Insertion into / Update dict: O(1)
        for loop: O(n), n: length of both words
    Special case checks: O(1)
    Dictionary comparison: O(n)
    
    >> O(n)
"""
