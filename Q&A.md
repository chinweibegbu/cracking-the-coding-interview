# Questions and Answers

### Arrays and Strings
1. What is the time complexity of hashtable insertion?
   <br> **O(1)** - Insertion, deletion and retrieval are all O(1) for a hash table

2. What is the time complexity of hashtable access?
   <br> **O(1)** - Also applies to `key in dict` checks

3. What is the time complexity of hashtable comparison?
   <br> **O(n)** *

4. Does Python have inbuilt sort function?
   <br>`sorted()`

5. What is the in-built function for creating a single string for an array/list?
   <br>`joiner.join(iterable_to_join)`, NOT `iterable_to_join.join(joiner)`

6. Which is bigger: O(n) or O(n logn)?
   <br> **O(n logn)** - It will dominate `n` in `O(n + nlogn)`

7. What is the time complexity of Python's `len()`?
   <br> **O(1)**

8. What is the time complexity of Python's string comparison?
   <br> **O(n)** *

9. How do you specify spacing when using `.format()`?
   <br> See https://www.geeksforgeeks.org/fill-a-python-string-with-spaces/

10. What is the Python in-built function to check if one string is a substring of the next?
   <br> ` substring in string`, NOT `string.contains(substring)` (Note that Python is case-sensitive i.e. `"love"` will NOT match `"Love"`)

11. What is the Python in-built function to find the index of a character in a string?
   <br> `string.index(substring)`

### Linked Lists

12. What is the runtime of an operation with an O(n) and an O(n-k) operation? Assume that k is positive.
   <br>
    * **O(n)** where is `n` is always greater than `k` 
    * **O(k)** where is `n` is always less than `k`
    * **O(n+k)** regardless of their relative values
  
13. Does Python have an in-built linked list structure?
   <br> No but, according to [this StackOverflow post](https://stackoverflow.com/questions/19752134/is-there-a-linked-list-predefined-library-in-python), you can simulate it with other structures like `collections.deque` 

### Stacks and Queues
14. How do you throw an error in Python?
    <br> `raise Exception(...)`

15. How do you refer to negative infinity in Python?
   <br> Import the `math` library and use the `inf` constant (see more [here](https://www.w3schools.com/python/ref_math_inf.asp))

### Trees and Graphs
16. How do you `print()` in Python without an end-line character?
   <br> `print(..., end="")`

17. How do you indicate class inheritance in Python?
   <br> `class ChildClass(ParentClass):`

\* not sure