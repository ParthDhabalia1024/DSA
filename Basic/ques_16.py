#Python program to remove all character from string except alphabets

str = "p@rth$dh@bali@*"
r=""

for char in str:
    if char.isalnum():
        r+= char

print(r)    