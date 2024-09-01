#Python program to count the number of vowels in a string 

string = "AryanKoli"
vowels = ["a", "e", "i" ,"o", "u", "A", "E", "I", "O","U"]

koli = ""

for char in string:
    if char in vowels:
        koli += char
        

print(koli)
print(len(koli))