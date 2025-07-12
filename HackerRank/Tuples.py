# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    
    n = int(input())                      
    integer_list = map(int, input().split())  
    t = tuple(integer_list)              
    print(hash(t)) 

    # for number in range(len(l)):
    #     print(l[number])

    # print(str(hash(t)))