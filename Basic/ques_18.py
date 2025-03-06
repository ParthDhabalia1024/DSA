#calculate factors

n = int(input())
# n2 = int(input())
# n3 = int(input())
def Factor(n):
    k=[]
    for i in range(1, n+1):
        if n % i == 0:
            k.append(i)
    return k
    
result = Factor(n)
print(result)        
