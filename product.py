class Product(object):
    def __init__(self,price,name,weight,brand,status='for sale'):
        self.price=price
        self.name=name
        self.weight=weight
        self.brand=brand
        self.status=status
    def sell(self):
        self.status='sold'
        return self
    def add_tax(self,tax_rate):
        self.price=self.price*(1+tax_rate)
        return self.price
    def return_product(self,reason):
        if reason=='defective':
            self.status='defective'
            self.price=0
        elif reason=='in box':
            self.status='for sale'
        elif reason=='out box':
            self.status='used'
            self.price=self.price*0.8
        return self
    def display_info(self):
        for key in self.__dict__:
            print "{} : {}".format(key,self.__dict__[key])
        print ""
        return self



product1=Product(100,'computer','20lb','apple')
product2=Product(200,'phone','0.2lb','sumsung')
# print product.add_tax(0.12)

# product.sell().return_product('out box').display_info()

class Store(object):
    def __init__(self,products,location,owner):
        self.products=products
        self.location=location
        self.owner=owner
    def add_product(self,product):
        self.products.append(product)
        return self
    def remove_product(self,product_name):
        for item in self.products:
            if item.name==product_name:
                self.products.remove(item)
        return self
    def inventory(self):
        for item in self.products:
            item.display_info()
        return self


store=Store([product1],'burbank','edmond')
store.inventory()
print "-----------------------"
store.add_product(product2)
store.inventory()
print "-----------------------"
store.remove_product('computer')
store.inventory()