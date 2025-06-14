def factorial(num):

    fact = 1
    if num == 0 | num ==  1:
        return f"Bilangan Factorial dari {num} = {fact}"
    else:
        for x in range(1, num + 1):
            fact *= x
    
    return f"Bilangan Factorial dari {num} = {fact}"
    

print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(1))
print(factorial(-20))


        