t = int(input())
for _ in range(t):
    n = int(input())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    # jika nilai max a lebih besar dari 
    # nilai max b maka print -1
    if max(a_arr) > max(b_arr):
        print(-1)
    else:
        for i in range(n):
            if b_arr[i] >= a_arr[i]:
                a_arr[i] += b_arr[i] - a_arr[i]
                if i == n-1:
                    print(0)
                    break
            
                



                
    

