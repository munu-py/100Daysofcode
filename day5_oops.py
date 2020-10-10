class Parrot:
    counter=0
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
    def set_name(self,value):
        self.__name=value
    def get_name(self):
        return self.__name
    def set_color(self,value):
        self.__color=value
    def get_color(self):
        return self.__color
    def display(self):
        unique_number=7001
        unique_number+=Parrot.counter
        Parrot.counter += 1
        print(self.__name,self.__color,unique_number)
p1=Parrot("ana","red")
p2=Parrot("dnd","green")
p1.display()
p2.display()



