n = int(input()) 
words = []
if n == 1:
    print("I hate it") 
else:
    for i in range(1,n+1) :
        if i == n:
            if i%2 == 0:
                words.append("I love it") 
            else:
                words.append("I hate it")
        else:
            if i%2 == 0:
                words.append("I love") 
            else:
                words.append("I hate")
    print(" that ".join(words))





# # Kode yg lebih cepat
# n = int(input()) 
# words = []
# for i in range(1,n+1) :
#     if i%2 == 0:
#         words.append("I love") 
#     else:
#         words.append("I hate")
# print(" that ".join(words) + " it")
