##class Student:
##    def __init__(self,rollno,name):
##        self.rollno=rollno
##        self.name=name
##    def displayname(self):
##        print("name is: ",self.name)
##
##st=Student(21,"suba")
##print("rollno is: ",st.rollno)
##
##st.displayname()

class Batch1:

    def __init__(self,name,batch,age):
        self.__name=name
        self.__batch=batch
        self.__age=age
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def displaynameage(self):
        print("Name and age is: ",self.__name,self.__age)

class Batch2(Batch1):
    def __init__(self,name,batch,age):
        super().__init__(name,batch,age)
    def displaybatch(self):
        print("Batch is: ")
b=Batch1("suba",2,21)
b.displaynameage()
print(b.getName())
b.setName("anusuya")
print(b.getName())
b.

        
    
