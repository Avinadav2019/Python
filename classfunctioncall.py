#creating class
class Student:
    #defining class variables
    name="Rocky"
    roll=205
    marks=85.6
    #defining function
    def showInfo(self):
        print("Name:",self.name)
        print("Rollno:",self.roll)
        print("Marks:",self.marks)

#creating object
s1=Student()
#calling function of class
s1.showInfo()
