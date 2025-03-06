# num = int(input("Enter the number : "))
# a = [10, 89, 9, 56, 4, 80, 8]
# string = "parthdhabalia"
# vowels = ["a", "e", "i" ,"o", "u", "A", "E", "I", "O","U"]
# arr = ["2", "8", "5", "9", "5", "6"]
from collections import Counter
num = input()
def reduce(num):
    r = ''
    counter = Counter(num)
    for key, value in counter.items():
        r += f"{key} occurs {value} times \n"

    return r
print(reduce(num))