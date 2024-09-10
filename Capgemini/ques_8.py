#Calculate the sum of number


n = int(input())
k = 0

for digit in str(n):
    k+=int(digit)
    
print(k)