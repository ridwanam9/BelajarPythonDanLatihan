n = int(input())
st = input()
anton = st.count("A")
danik = st.count("D")

if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")
