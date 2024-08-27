
try:
    print("Star of the method")
    #raise TypeError("Custorm error")
except ZeroDivisionError as er:
    print("Exception in method")
except Exception as er:
    print("Type exception in method")
    print(er)
else:
    print("End of method")
print("Test after exception")
