#calculate the length of the string

def calculatelength(n):
    k=0
    for char in n:
        k+=1
    return k

n = input()
print(calculatelength(n))