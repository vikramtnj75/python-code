import os
from os.path import exists
from pathlib import Path
from Functions import AstricsParam
try:

    #value=open("C://Users/Pranavika/OneDrive/Desktop/test.txt","r")
    #print(value.read())

    #with open("C://Users/Pranavika/OneDrive/Desktop/test.txt","r") as values:
     #   for val in values.readlines():
      #      print(val)
    #values.close()

    #value=open("C://Users/Pranavika/OneDrive/Desktop/test1.txt","w")
    #value.writelines("Append from code")

    #print(exists("C://Users/Pranavika/OneDrive/Desktop/test2.txt"))
    #print(Path("C://Users/Pranavika/OneDrive/Desktop/test1.txt").is_file())
    src="C://Users/Pranavika/OneDrive/Desktop/test.txt"
    destination="C://Users/Pranavika/OneDrive/Desktop/"
   # os.rename(src,destination)
    #os.remove(destination)
   # print(os.path.getsize(src))

   # for root, dirs, files in os.walk(destination):
    #    print(files)

    AstricsParam.add(1)

except Exception as e:
    print(e)