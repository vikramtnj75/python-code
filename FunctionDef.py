#def add(valueOne,valueTwo=45):    
    #print(valueOne+valueTwo)
#    return valueOne+valueTwo

#sumvalue=add(12)
#print(sumvalue-10)

#def greeting(name,message):
#    print(message + name)

#greeting('Test', 'Welcome to Python ')
#greeting(message='Welcome to Python ', name='Test')

def calculate(count):    
   "Return the sum of two arguments"
   return lambda value: value *count
    
val=calculate(2,10)
print(val)