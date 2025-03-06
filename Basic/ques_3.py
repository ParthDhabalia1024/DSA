#Find the Sum of the First N Natural Numbers in Python

n = int(input())
# sum = int((n*(n+1)) / 2)

def sum(n):
    k=0
    for i in range(0, n+1):
        k+=i
    return k

print(sum(n))
