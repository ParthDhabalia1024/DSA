#check weather the number is prime or not

def isprime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
print(isprime(n))
