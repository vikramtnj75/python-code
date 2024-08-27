from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]
name=['Test4','Test2']
#print(name)
#print(name[0])
#for val in name:
#    print(val)
#name.append('Test1')
#print(name)
#name.insert(1,'Test')
#print(name)
#name[1]='Test5'
#print(name)
#del name[1]
#name.pop()
#name.remove('Test2')
#print(name)
#name.sort(reverse=True)
#value =sorted(name)
#print(name)
#print(value)
#print(name[0:2])
#print(numbers[0:9:3])
#print(name[-3])
#print(len(name))

#--name=['Test4','Test2']

a, b=name
#print(a)

#for val in name:
#    print(val)
    
#for index,value in enumerate(name):
#    print(str(index) + '--'+ value)

#filterValues=filter(lambda val:val=='Test4', name)
#print(filterValues)
#print(list(filterValues))

#def add(val1, val2):
#    return val1+val2
#value=0
#for va in numbers:
#    value=add(value+va)

reduceValues=reduce(lambda val1, val2: val1+val2, numbers)
print(reduceValues)







