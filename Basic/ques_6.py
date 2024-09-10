#Find the Factorial of a Number in Python Language


n = int(input())

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact*i
#     return fact

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(n))
