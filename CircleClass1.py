class Rectangle:
    length=5
    bredth=2
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def setlength(self,length):
        self.length=length
    def setbredth(self,bredth):
        self.bredth=bredth
    def getArea(self):
        print("Area of rectangle is: ",self.length*self.bredth)
r=Rectangle()
r.getArea()
r.setlength(3)
r.getArea()
