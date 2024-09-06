#Problem Statement –

# You’re given an array of integers, print the number of times each integer has occurred in the array.
#Input :

# 10

# 1 2 3 3 4 1 4 5 1 2

 

# Output :

# 1 occurs 3 times

# 2 occurs 2 times

# 3 occurs 2 times

# 4 occurs 2 times

# 5 occurs 1 times
from collections import Counter
n=int(input())
arr = list(map(int, input().split()))

def countofoccurance(n,arr):
    counter = Counter(arr)
    result = ''
    for key,value in counter.items():
        result+= f'{key} occurs {value} times\n'
    return result
print(countofoccurance(n,arr))
