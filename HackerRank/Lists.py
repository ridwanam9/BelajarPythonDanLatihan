if __name__ == '__main__':
    nlist = []  
    N = int(input())
    
    for _ in range(N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            i = int(cmd[1])
            e = int(cmd[2])
            nlist.insert(i, e)
        elif cmd[0] == "print":
            print(nlist)
        elif cmd[0] == "remove":
            e = int(cmd[1])
            nlist.remove(e)
        elif cmd[0] == "append":
            e = int(cmd[1])
            nlist.append(e)
        elif cmd[0] == "sort":
            nlist.sort()
        elif cmd[0] == "pop":
            nlist.pop()
        elif cmd[0] == "reverse":
            nlist.reverse()
