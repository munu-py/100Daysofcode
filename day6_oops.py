class Freight:
    freight_id=198
    def __init__(self,customer):
        self.freight_charge_w=None
        self.freight_charge_d=None
        self.customer=customer
    def forward_cargo(self):

        if (self.customer.validate_weight()==True and self.customer.validate_customer_id()==True and self.customer.validate_distance()==True):

            Freight.freight_id+=2
            self.freight_charge_w=self.customer.weight*150
            self.freight_charge_d=self.customer.distance*60

        else:
            self.freight_charge_w=0
            self.freight_charge_d=0

class Customer:
    def __init__(self,customer_id,weight,distance):
        self.customer_id=customer_id
        self.weight=weight
        self.distance=distance
    def validate_customer_id(self):
        if (len(str(self.customer_id))==6 and str(self.customer_id)[0]==str(1)):
            return True
        else:
            return False
    def validate_weight(self):
        if(self.weight%5==0):
            print("weight pass")
            return True
        else:
            print("false")
            return False
    def validate_distance(self):
        if(self.distance>=500 and self.distance<=5000):
            print("dist pass")
            return True
        else:
            print("false")
            return False
c1=Customer(123456,20,600)
c1.validate_weight()
c1.validate_distance()
f=Freight(c1)
f.forward_cargo()
print(Freight.freight_id)
print(f.freight_charge_w,f.freight_charge_d)
c2=Customer(123457,30,700)
f1=Freight(c2)
f1.forward_cargo()
print(Freight.freight_id)
print(f1.freight_charge_d,f1.freight_charge_w)