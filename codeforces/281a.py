st = list(input())
first_word = st[0].upper()
st.remove(st[0])
print(first_word+"".join(st))
