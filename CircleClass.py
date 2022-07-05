class Circle:
    radius=0
    def __init__(self,radius):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of a Circle is ",self.radius,"radius ",3.14*(self.radius**2))

radius=int(input("enter a radius value"))        
c=Circle(radius)
c.getArea() 
c.setRadius(15)
c.getArea()
