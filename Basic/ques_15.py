# #check weather the given number is prime or not

def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, n):
        if n % i == 0:
            return False  # Divisible by a number other than 1 and itself
    return True  # No divisors found, it's a prime number

print(is_prime(2))

