# Coding Question 6
# A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

# You are required to implement the following function, Int NumberOfCarries(int num1 , int num2);

# The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of 
# carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

# Assumption: num1, num2>=0

# Example:

# Input
# Num 1: 451
# Num 2: 349
# Output
# 2
# Explanation:

# Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

# Sample Input

# Num 1: 23

# Num 2: 563

# Sample Output

# 0

def Numberofcarries(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    carry = 0
    carry_count = 0
    
    # Ensure both numbers have the same length by padding with zeros
    num1 = num1.zfill(max(len(num1), len(num2)))
    num2 = num2.zfill(max(len(num1), len(num2)))

    # Traverse the numbers from the last digit to the first
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        if digit_sum > 9:
            carry = 1
            carry_count += 1
        else:
            carry = 0

    return carry_count

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Number of carry operations:", Numberofcarries(num1, num2))
