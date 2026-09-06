t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    brr = input()
    a_pos = []
    b_pos = []
    for i in range(n):
        if arr[i] == "1":
            if i % 2 == 1:
                a_pos.append(1)
            else:
                a_pos.append(2)
        if brr[i] == "1":
            if i % 2 == 1:
                b_pos.append(1)
            else:
                b_pos.append(2)
                
    if sorted(a_pos) == sorted(b_pos):
        print("Yes")
    else:
        print("No")