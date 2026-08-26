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
names = [[] for _ in range(9)]


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

def remove(name):
    position = index_position(name)
    names[position].remove(name)

def check_name(name):
    return f"{name} is in the Hash Table: {contains(name)}"

add('Stuart')
add('Helda')
add('Johan')
add("Yusuf")

print(names)
print(check_name("Helda"))

remove('Helda')

print(names)
print(check_name("Helda"))
