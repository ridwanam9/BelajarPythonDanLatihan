# Membuat Class
class Myclass:
    x = 5


# Membuat Object
p1 = Myclass()
p2 = Myclass()
p3 = Myclass()


print(Myclass)
print(Myclass.x)
print(p1.x)
print(p2.x)
print(p3.x)

# Menghapus Class
del p1



# Pass Statement
# Class tidak boleh kosong, jika perlu menambahkan 
# class tanpa konten apapun, tambahkan pass agar menghindari error
class kosong:
    pass

print(kosong)





class person:
    species = "Human" # Class Property

    def __init__(self, name, age, city = "Pontianak"):
        self.name = name # Intance Property
        self.age = age
        self.city = city

    def name_person(self):
        print(f"Hello, {self.name}. ")

    def greed(self):
        identity = self.name_person()
        print(f"{identity} I'm {self.age} years old")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday, You're are now {self.age}")


orang = person("Budi", 56)
orang.country = "Indonesia" # Add Property to existing object

orang2 = person("Ridwan", 18, "jakarta")
orang3 = person("Johan", 20)
orang4 = person("Erda", 21)
orang5 = person("Lala", 26)



print(orang)
print(orang.name)
print(orang.age)
print(orang.city)
print(orang.species)
print(orang.country)

print("-------------")

print(orang2.name)
print(orang2.age)
print(orang2.city)
print(orang2.species)

print("-------------")

print(orang3.name)
print(orang3.age)
print(orang3.city)
print(orang3.species)

print("-------------")

orang4.greed()
# Memodifikasi properti
orang4.age = 25
orang4.greed()
print(orang4.species)

print("-------------")

print(orang5.name)
print(orang5.age)
print(orang5.city)
print(orang5.species)
orang5.celebrate_birthday()



# print("--------Error---------")
# # menghapus properti
# del orang4.age
# orang4.greed() # error




class calculator:
    def add(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b

calc = calculator()
print(calc.add(3, 5))
print(calc.multiply(4, 7))

