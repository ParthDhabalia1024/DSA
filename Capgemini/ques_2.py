#Problem Statement –

# Capgemini in its online written test have a coding question, wherein the students are given a string with multiple characters 
# that are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

# Input :

# aabbbbeeeeffggg

# Output:

# a2b4e4f2g3
from collections import Counter

n = input()
def count(n):
    counter = Counter(n)
    result = ''
    for key, value in counter.items():
        result +=f'{key}{value}'
    return result

print(count(n))