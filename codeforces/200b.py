n = int(input())
arr = list(map(int, input().split()))
orange_frac = 0
for i in range(n):
    orange_frac += arr[i]/100
hasil = (orange_frac/n)*100
print(f"{hasil:.12f}")