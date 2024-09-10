# Problem Statement –

# You have write a function that accepts, a string which length is “len”, the string has some “#”, 
# in it you have to move all the hashes to the front of the string and return the whole string back and print it.

# example :-

# Sample Test Case

# Input:

# Move#Hash#to#Front

# Output:

# ###MoveHashtoFront

p = str(input())
s = p.count('#')
a = p.replace("#", "")
print('#'*s+a)
