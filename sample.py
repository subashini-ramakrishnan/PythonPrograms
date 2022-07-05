
class Mouse:
    length=5
    breadth=3
    weight=50
    clour="black"
    def leftClick(s):
        print("leftclicked")
        print(s.length)
    def rightClick(s):
        print("rightclicked")
    def scroll(s):
        print("scrolled")
dell=Mouse()
dell.leftClick()
dell.rightClick()
dell.scroll()
print(dell.clour)
dell.clour="red"
print(dell.clour)

