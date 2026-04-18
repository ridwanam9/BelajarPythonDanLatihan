# https://codeforces.com/problemset/problem/2217/A

# A. The Equalizer
# time limit per test1 second
# memory limit per test256 megabytes

# To settle a long-time feud, Shaunak and Yash decided to play a game on an array a
#  of n
#  integers, with Shaunak going first. The players take turns, and the last player to make a move wins. On a player's turn, he chooses some ai>0
#  and decrements it by 1
# .

# To make things interesting, Shaunak is allowed to use a special move at most once during the game. This move replaces his normal turn. When used, all elements ai
#  (1≤i≤n
# ) are set to a special value k
#  that is given initially.

# Assuming that both players play optimally, determine if Shaunak can always win.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (1≤n≤100
# , 1≤k≤500
# ), denoting the size of the array and the special value.

# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤103
# ).

# Output
# For each test case, print "YES" if Shaunak can always win, and "NO" otherwise.

# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

# import random

# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))

#     steps = sum(a)
#     is_k_thrown = False
#     random_step = random.randrange(0, steps) #take one random step to change all items in the list 

#     for i in range(steps+1):
#         if i == random_step:
#             is_k_thrown = True

#     if is_k_thrown == True:
#         a[:] = [k] * len(a) #change all items in a list into k value
#         if sum(a)%2==0 or sum(a)==1:
#             print("yes") 
#         else:
#             print("no") 
#     else:
#         if sum(a)%2==0 or sum(a)==1:
#                 print("yes") 
#         else:
#             print("no") 

                

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    steps = sum(a)
    if steps % 2 == 1 or (n * k) % 2 == 0:
        print("YES")
    else:
        print("NO")