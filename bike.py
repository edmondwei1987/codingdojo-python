class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
    def displayInfo(self):
        print "bike's price is {},maximum speed is {},total miles is {} now.".format(self.price,self.max_speed,self.miles)
    def ride(self):
        print "Riding"
        self.miles=self.miles+10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles>5:
            self.miles=self.miles-5
        return self

bike1=Bike(50,"25mph")
bike2=Bike(100,"30mph")
bike3=Bike(200,"35mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().displayInfo()