# #print sum of all even numbers and odd number
# arr = ["2", "8", "5", "9", "5", "6"]

# def sum_even(arr):
#     e = 0
#     for i in range(0, len(arr)):
#       num = int(arr[i])
#       if num % 2 == 0:
#         e=e+num
#     return e
# def sum_odd(arr):
#     o = 0
#     for i in range(len(arr)):
#        num = int(arr[i])
#        if num % 2 != 0:
#         o+=num
#     return o

# print("Sum of even:", sum_even(arr))
# print("Sum of odd:", sum_odd(arr))








#print floyds triangle
def floyds_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()  # Move to the next line after each row

# Example usage:
floyds_triangle(5)




#print pascals triangle
def pascals_triangle(rows):
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        print(" ".join(map(str, row)))
        prev_row = row

# Example usage:
pascals_triangle(5)


# #check leap year

# p = int(input())

# def is_leap(p):
#     if p % 4 == 0:
#         return True
#     elif p % 100 == 0:
#         return True
#     else:
#         return False
# print(is_leap(p))









#reverse array and print positions in string format 

