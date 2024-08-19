def sumDivisibleBy(n):
    """
    function to get sum of number divisble by n

    series formula = S = 1 + 2 + 3 + 4 +5 + ... + n = n(n + 1) // 2

    deviation:
        S = 1 + 2 + 3 + ... + n
        S = n + (n - 1) + (n - 2) + ... +1
        2S = (1 + n) + (2 + (n -1)) + 3 + (n - 2)+ ... + (n + 1)
        2S = n(n + 1)
        S = n(n + 1)//2
    """
    p = 999 // n
    return n * (p * (p + 1)) // 2


res = sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
print(res)
