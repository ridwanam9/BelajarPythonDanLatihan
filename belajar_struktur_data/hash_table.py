# names = [[]]*10
# names = [
#   [],
#   [],
#   [],
#   [],
#   [],
#   [],
#   [],
#   [],
#   [],
#   []
# ]
# names = [[]]*10
names = [[] for _ in range(9)]
# print(names)
# print(names1)

def index_position(name):
    count = 0
    for x in name:
        count += ord(x)
    return count % 10

def add(name):
    position = index_position(name)
    names[position].append(name)

def contains(name):
    position = index_position(name)
    # return names[position] == name #akan menghasilkan false karena membandingkan names[position] = list dengan name = string 
    return name in names[position]



add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
add('Helda')
add('Johan')
add("Yusuf")
print(names)
print("'Pete' is in the Hash Table:", contains("Pete"))
print("'Jones' is in the Hash Table:", contains("Jones"))
# add("Noah")
# print(names)
