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
#Inheriting Square into Triangle
class Triangle(Square):
    #defining function
    def tri_area(self,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle:",area)
#creating object derived class
obj=Triangle()
obj.rec_area(10,20)
obj.squ_area(12)
obj.tri_area(12,25)
