def swap_case(s):
    swap_s = s.swapcase()
    return swap_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)