def smallest_divible() -> int:
    n = 11
    while n < 100000000:
        # print(n)
        if all([n % i==0 for i in range(1,20) if i % 2==0]):
            return n
        n += 1
    

print(smallest_divible())
        

    
            
