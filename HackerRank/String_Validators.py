import re
if __name__ == '__main__':
    s = input()
    
    print(bool(re.search(r'[a-zA-Z0-9]', s)))
    print(bool(re.search(r'[a-zA-Z]', s)))
    print(bool(re.search(r'\d', s)))
    print(bool(re.search(r'[a-z]', s)))
    print(bool(re.search(r'[A-Z]', s)))
