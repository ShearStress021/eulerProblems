def is_prime(n):
    """
    A prime number that is divible by 1 and it self
    """
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

if is_prime(8):
    print("hey there")


def largest_prime_factor(n):
    if n % 2 == 0:
        n = n / 2
        lastFactor = 2
        while n % 2 == 0:
            n = n / 2
    else:
        lastFactor = 1

    factor = 3
    while n > 1:
        if n % factor == 0:
            n = n / factor
            lastFactor = factor
            while n % factor == 0:
                n = n / factor
        factor = factor + 2
    return lastFactor
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
print(largest_prime_factor(20))
