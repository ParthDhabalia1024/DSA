#Python Program to Remove Vowels from a String

string = "AryanKoli"
vowels = ["a", "e", "i" ,"o", "u", "A", "E", "I", "O","U"]
res = ""

for char in string:
    if char not in vowels:
        res = res + char

print(res)