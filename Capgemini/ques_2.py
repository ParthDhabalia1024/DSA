#Problem Statement –

# Capgemini in its online written test have a coding question, wherein the students are given a string with multiple characters 
# that are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

# Input :

# aabbbbeeeeffggg

# Output:

# a2b4e4f2g3
from collections import Counter

n = input()
def reduce(n):
    r=''
    counter = Counter(n)
    
    for key,value in counter.items():
        
        r += f"{key}{value}"
    return r

print(reduce(n))