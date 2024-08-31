#Check Whether a Number is Even or Odd in Python
a = int(input("Enter the number  "))

def EvenOdd(nums):
    if nums % 2 == 0:
        return 'even'
    elif nums % 2 != 0:
        return 'odd'
    else:
        return 0

result = EvenOdd(a)    
print(result)

