# import re
if __name__ == '__main__':
    s = input()

    # Menggunakan perulangan
    list_isalnum = []
    list_isalpha = []
    list_isdigit = []
    list_islower = []
    list_isupper = []

    for i in s:
        if i.isalnum() == True:
            list_isalnum.append("True")
        else:
            list_isalnum.append("False")
    for i in s:
        if i.isalpha() == True:
            list_isalpha.append("True")
        else:
            list_isalpha.append("False")
    for i in s:
        if i.isdigit() == True:
            list_isdigit.append("True")
        else:
            list_isdigit.append("False")
    for i in s:
        if i.islower() == True:
            list_islower.append("True")
        else:
            list_islower.append("False")
    for i in s:
        if i.isupper() == True:
            list_isupper.append("True")
        else:
            list_isupper.append("False")

    list_isalnum.sort(reverse=True)
    list_isalpha.sort(reverse=True)
    list_isdigit.sort(reverse=True)
    list_islower.sort(reverse=True)
    list_isupper.sort(reverse=True)
  
    print(list_isalnum[0])
    print(list_isalpha[0])
    print(list_isdigit[0])
    print(list_islower[0])
    print(list_isupper[0])

    # # Menggunakan regex
    # print(bool(re.search(r'[a-zA-Z0-9]', s)))
    # print(bool(re.search(r'[a-zA-Z]', s)))
    # print(bool(re.search(r'\d', s)))
    # print(bool(re.search(r'[a-z]', s)))
    # print(bool(re.search(r'[A-Z]', s)))
