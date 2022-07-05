class Phone:
    def __init__(self,name,brand,price,color,mode):
        self.name=name
        self.brand=brand
        self.price=price
        self.color=color
        self.mode=mode
    def makeCall(self):
        print("calling..")
    def incoming(self):
        print("Ringing")
class Mobile(Phone):
    def __init__(self,name,brand,price,color,mode,battery):
        super().__init__(name,brand,price,color,mode)
        self.battery=battery
    def gaming(self):
        print("start the game")
        super().makeCall()
        Phone.makeCall(self)
    def messaging(self):
        print("send message")
    def calculator(self):
        print("make calculation")
    def video(self):
        print("play video")
class SmartPhone(Mobile):
    def __init__(self,name,brand,price,color,mode,battery,ram,internet,display):
        super().__init__(name,brand,price,color,mode,battery)
        self.ram=ram
        self.internet=internet
        self.display=display
    def app(self):
        print("you can access your app")
    def selfie(selfie):
        print("Take a selfie")
usage=Phone("maxi","lava",8000,"black","wireless")
usage.incoming()
s=SmartPhone("maxi","lava",8000,"black","wireless","lava",7,"yes","15cm")
s.ram=5
print(s.ram)
s.gaming()



    
