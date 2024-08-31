#Python program to Sort first half in ascending order and second half in descending order in an array

a = [10, 89, 9, 56, 4, 80, 8]
a.sort()
n = len(a)

def sort_ascdesc(a,n):
    
    i = 0
    while i < n/2:
        print (a[i])
        i = i+1
    j = n-1
    while j > n/2:
        print(a[j])
        j -= 1

print(sort_ascdesc(a,n))    

