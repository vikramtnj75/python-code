bankDetails={"name":"SBI", "accountType":"Saving", "brach":"Chennai","ifscCode":"34567"}

#print(bankDetails['nameTest'])
#print(bankDetails.get('nameTest'))

bankDetails["key"]="Value"


bankDetails["key"]="Value new"

del bankDetails["key"]

#print(bankDetails)

#for ind, val in bankDetails.items():
#    print(val)

#for  val in bankDetails.keys():
#    print(val)

for  val in bankDetails.values():
    print(val)