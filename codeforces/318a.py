n, k = map(int, input().split())
odds = []
evens = []
for i in range(1, n+1):
    if i%2 == 1:
        odds.append(i)
    else:
        evens.append(i)
arr = odds + evens
print(arr[k-1])