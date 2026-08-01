t = int(input())
for _ in range(t):
    n, a, b, k = map(int, input().split())
    if k >= a and k >= b:
        if a == k and b == k:
            print(n)
        elif k%a==0 and k%b==0:
            if b>a:
                print((n//2)+1)
            # elif a>b:
                # kalo a sudah matang maka b pindah ke a
                # saat nya membuat rumus sendiri





    elif a > k and b > k:
        print(0)
    elif a > k and b == k:
        print(n//2)
    elif a == k and b > k:
        if n%2==0:
            print(n/2)
        else:
            print((n//2)+1)



    


    
    