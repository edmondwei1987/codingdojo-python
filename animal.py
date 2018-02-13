class Animal(object):
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def display_health(self):
        print self.health

# animal=Animal('wa',30)
# animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self,name,health=150):
        super(Dog,self).__init__(name,health=150)

    def pet(self):
        self.health+=5
        return self

dog=Dog('ma')
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self,name,health=170):
        super(Dragon,self).__init__(name,health=170)
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        print "I am a Dragon"
        super(Dragon,self).display_health()

dragon=Dragon('da')
dragon.fly().run().display_health()

class Snake(Animal):
    pass
snake=Snake('fo',200)
snake.run().display_health()