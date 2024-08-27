print("Test before")

try:
    #print(10/1)
   # float("tt")
    raise TypeError("Test raise")
except ArithmeticError as zero:
    print("Exception in method")    
except ValueError as value:
    print("Value exception in method")    
except TypeError as err:
    print("Type exception in method")    
    print(err)
else:
    print("Else block")
finally:
    print("Finally block")

print("Test after")