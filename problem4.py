def largest_palindrome(n: int) -> int:
    res, larg = 1, 1
    j = n
    while j >= 100:
        i = n
        while i >= 100:
            res = j * i
            if str(res) == str(res)[::-1]:
                larg = max(larg, res)
            i -= 1
        j -= 1

    return larg


    
print(largest_palindrome(999))
