def check_permutation(s1, s2):
    # If strings are not the same length, they are not permutations
    if (len(s1) != len(s2)): return False
    
    # If strings are the same, they are permutations 
    if (s1 == s2): return True
    
    # Sort both strings (assume O(nlogn) runtime for the in-built function)
    s1_sorted, s2_sorted = sorted(s1), sorted(s2)
    
    # The strings are permutations if their sorted forms are the same
    return s1_sorted == s2_sorted

print(check_permutation("faab", "baa"))
print(check_permutation("kla", "kla"))
print(check_permutation("ab", "ba"))

"""
Runtime Analysis:
    Sorting: O(nlogn)
    Special case checks: O(1)
    String comparison: O(n)
    
    >> O(nlogn)
    CONCLUSION: Performs worse than v1
"""
