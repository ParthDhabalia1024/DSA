#Find Largest element in an array using Python

a = [10, 89, 9, 56, 4, 80, 8]

def max_element(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

print(max_element(a))

