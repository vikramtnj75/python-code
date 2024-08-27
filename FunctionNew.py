def add(valueOne, valueTwo=50):   
    "This is goin to add two numbers"
    print('valueOne --'+str(valueOne))
    return valueOne+valueTwo

#c=add(10,30)
#print(c)

def recurPrintNumber(value):
    print(value)
    if(value<10):
        value=value+1
        recurPrintNumber(value)

#recurPrintNumber(0)

adding= lambda valueOne,valueTwo : valueOne+valueTwo

print(adding(10,30))