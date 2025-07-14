def print_formatted(number):

    width = len(str(bin(number))[2:])
    for i in range(1, number + 1): 
        txt1 = "{0:d}"
        txt2 = "{0:o}"
        txt3 = "{0:X}"
        txt4 = "{0:b}"
        print(txt1.format(i).rjust(width), end=" ")
        print(txt2.format(i).rjust(width), end=" ")
        print(txt3.format(i).rjust(width), end=" ")
        print(txt4.format(i).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)