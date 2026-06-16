n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

is_all_true = True
for i in range(n):
    true_owner = b[a[i] - 1]  
    if true_owner != i + 1:     
        is_all_true = False
        break

print("Yes" if is_all_true else "No")
