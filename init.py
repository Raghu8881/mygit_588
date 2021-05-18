class Car:
    def __init__(self,modelname,yom,price):
        self.m=modelname
        self.y=yom
        self.p=price
    def price_in(self) :
        self.o=int(self.p*1.5)   
honda=Car('city',2017,1000000)
tata=Car('bolt', 2016, 800000)
print(honda.p)
honda.price_in()
print(honda.o)