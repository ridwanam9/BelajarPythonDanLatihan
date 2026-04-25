from collections import Counter
  
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# with dictionary
count = Counter({'A':3, 'B':5, 'C':2})
print(count)

count.update(['A', 1])
print(count)


list_ini = ["Geeks", "For", "Geeks"] 
print(Counter(list_ini))