class Apparel:
    counter=100
    def __init__(self,item_type,price):
        self.item_type=item_type
        self.price=price
        if(self.item_type=="Cotton"):
            Apparel.counter+=1
            self.item_id="C"+str(Apparel.counter)
        elif(self.item_type=="Silk"):
            Apparel.counter += 1
            self.item_id = "S" + str(Apparel.counter)

    def calculate_price(self):
        self.price=self.price+ (self.price*5)/100

class Cotton(Apparel):
    def calculate_price(self,discount):
        super().calculate_price()
        self.price=self.price-discount
        self.price=self.price+(self.price*5)/100


class Silk(Apparel):
    def calculate_price(self):
        super().calculate_price()
        if self.price>10000:
            self.points=5
        else:
            self.points=3
        self.price=self.price+(self.price*10)/100

c=Cotton("Cotton",100)
c.calculate_price(10)
s=Silk("Silk",12000)
s.calculate_price()
print(c.price,c.item_id)
print(s.price,s.points,s.item_id)

