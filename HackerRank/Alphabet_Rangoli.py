def print_rangoli(size):
    
    letters = []
    for i in range(ord('a'), ord('z') + 1):
        letters.append(chr(i))
        
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = "".join(letters)


    # top layer
    for j in range(n - 1, -1, -1):
        print(letters[j].rjust(n*2, "-"))
        # print(letters[j, -1, -1])
        

    # middle layer

    # bottom layer


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)