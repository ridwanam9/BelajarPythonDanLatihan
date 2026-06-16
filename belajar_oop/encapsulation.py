# In Python, you can make properties private by 
# using a double underscore __ prefix

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # print private property menggunakan getter methode
    def get_age(self):
        return self.__age
    
    # Set Private Property Value
    # To modify a private property, you can create a setter method.

    # The setter method can also validate the value before setting it:
    def set_age(self, edited_age):
        if edited_age >= 0:
            self.__age = edited_age
        else:
            print("Age must be positive")


p1 = Person("Emil", 25)

print(p1.name)

try:
    print(p1.__age) #tidak dapat diprint karena private property
except:
    print("Tidak dapat diprint, karena properti Private")


print(p1.get_age())
p1.set_age(27)

print(p1.get_age())


print("-"*10)
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")
            # return "Grade must be between 0 and 100"

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Email")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())