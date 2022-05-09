#creating class
class Rectangle:
    #defining function
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
#Inheriting Rectangle into Square
class Square(Rectangle):
    #defining function
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
#creating object derived class
obj=Square()
#calling base class function
obj.rec_area(10,20)
#calling derived class function
obj.squ_area(12)
