class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price>10000:
            self.tax=0.15
        else:
            self.tax=0.12
        self.display_all()
    def display_all(self):
        for key in self.__dict__:
            print key + ":" + str(self.__dict__[key])

car1=Car(2000,'45mph','Full','57mpg')
car2=Car(12000,'40mph','Half','68mpg')