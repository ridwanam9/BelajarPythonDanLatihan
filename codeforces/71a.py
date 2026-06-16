n = int(input())
for _ in range(n):
    text = input()
    if len(text) <= 10:
        print(text)
    else:
        print(f"{text[0]}{len(text)-2}{text[-1]}")