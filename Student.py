from Department import Department
from College import College
class Student(Department,College):

    def __init__(self,name,regNo):
        self.name=name
        self.regNo=regNo

    def getStudentDetails(self, age=None):
        print("Student details "+ self.name +" Reg No " +self.regNo + " age is "+str(age))    
    
    
    def getDepartment(self):
        print("Department from student")


student=Student('Test','12234')
student.getCollegeAddress()
student.getDepartment()
#student.getStudentDetails()
student.getStudentDetails()
student.common()