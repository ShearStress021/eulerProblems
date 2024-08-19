def fibonacci(n: int) -> int:
    a, b = 0, 1
    tots = 0
    while b < n:
        
        a , b = b , a + b
        if b % 2 == 0:
            tots += b
    return tots


print(fibonacci(4000000))







