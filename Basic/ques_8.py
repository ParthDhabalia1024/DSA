#Find Smallest element in an array using Python

a = [10, 89, 9, 56, 4, 80, 8]

def max_element(a):
    min = a[0]
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min

print(max_element(a))