#Python program to Sort first half in ascending order and second half in descending order in an array

a = [10, 89, 9, 56, 4, 80, 8]
# n2 = int(input())
# n3 = int(input())

def sort_asc_desc_element(a):
   mid = len(a) // 2
   first_half = sorted(a[:mid])
   second_half = sorted(a[mid:], reverse=True)
   
   return first_half + second_half
result = sort_asc_desc_element(a)
print(result)        

