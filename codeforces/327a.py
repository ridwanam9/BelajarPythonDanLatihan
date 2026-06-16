# Flipping Game
n = int(input())
arr = list(map(int, input().split()))

# arr = [1,0,0,1,0,1,0,0,0,0,1] # 9
# # out = [1,1,1,0,1,0,1,1,1,1,1]

# arr = [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1] # 8
# out = [1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]

# Mencari posisi semua angka 0
indices = []
for i in range(n):
    if arr[i] == 0:
        indices.append(i)

for x in range(indices[0], indices[-1]+1):
    arr[x] = 1-arr[x]
   
count = 0
for y in arr:
    if y == 1:
        count += 1

# print(indices)
print(*arr)
print(count)
    

# pertama cari semua posisi value 0
# 