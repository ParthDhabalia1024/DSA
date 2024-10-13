#Minimun absolute difference


a = [2, 5, 4, 3]
# b = [18, 23, 29, 95, 25]
def minimum_absolute_differece(a):
    a.sort()
    k=0
    mid =  a[len(a) // 2]
    for i in range(len(a)):
        a[i] = abs(mid - a[i])
        k+=a[i]
    return k 

    
print(minimum_absolute_differece(a))