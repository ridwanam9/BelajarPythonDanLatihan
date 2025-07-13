n_str, m_str = input().split()

N = int(n_str)
M = int(m_str)

# top layers
for x in range(1, N):
    if x % 2 != 0:
        print((".|."*(x)).center(M,"-"))

# middle layer
print("WELCOME".center(M, "-"))

# bottom layers
for x in range(N-1, -1, -1):
    if x % 2 != 0:
        print((".|."*(x)).center(M,"-"))


