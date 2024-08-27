def add(*value):
    print(value)
    sum=0
    for val in value:
        sum=sum+val
    print(sum)

add(1,2,3,4,5,6,7,8)

def bankDetails(**bank):
    print(bank)
    print(bank["name"])
    
bank={"name":"SBI", "accountType":"Saving", "brach":"Chennai","ifscCode":"34567"}
bankDetails(**bank)