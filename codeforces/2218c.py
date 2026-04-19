t = int(input())
for _ in range(t):
    n = int(input())
    
    l = 1
    r = 3 * n
    result = []
    
    for _ in range(n):
        result.append(l)      
        result.append(r - 1)  
        result.append(r)      
        
        l += 1
        r -= 2
    
    print(*result)