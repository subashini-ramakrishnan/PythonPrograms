class Rectange:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def getArearect(self):
        return self.length*self.bredth
class Qubaid(Rectange):
    def __init__(self,length,bredth,height):
        super().__init__(length,bredth)
        self.height=height
    def getAreaQube(self):
        print("Area of Qubaid: ",super().getArearect()*self.height)


space1=Qubaid(2,3,4)
space1.getAreaQube()
space1.getArearect()
print(space1.getArearect())

        
