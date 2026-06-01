# A NamedTuple returns a tuple object with names for each position which the 
# ordinary tuples lack. 
# For example, consider a tuple names student where the first element represents fname, 
# second represents lname and the third element represents the DOB. 
# Suppose for calling fname instead of remembering the index position you can actually call the element by 
# using the fname argument, then it will be really easy for accessing tuples element. This functionality is 
# provided by the NamedTuple.


from collections import namedtuple
    
# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
    
# Adding values
S = Student('Nandini','19','2541997')
Y = Student('Yusuf','26','2541987')
    
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
print (Y[1])
# print (S.age)
    
# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)
print (Y.name)



print (S)
print (Y)