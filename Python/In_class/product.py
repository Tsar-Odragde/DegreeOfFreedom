class Product:
    #def __str__(self, prod_id, market_price, discount):
    def __init__(self, prod_id, market_price, discount):
        self.prod_id = prod_id
        self.market_price = market_price
        self.discount = discount

    def selling_price(self):
        print(f"{self.market_price - 0.01 * self.discount * self.market_price}")

    def discount(self):
        print(f"{self.discount+2 if self.market_price > 500 else self._discount}")

    def discount(self, new_discount):
        self._discount = new_discount

    def display(self):
        print(f"{self.prod_id, self.market_price, self.discount}")

p1 = Product("ABC", 200, 7)
#p2 = Product(CD044, 750, 3)
#p3 = Product(GH254, 300, 5)
#p4 = Product(JG652, 600, 6)
p1.selling_price()
p1.display()
#print(p1.prod_id, p1.selling_price)
#print(p2.prod_id, p2.selling_price)
#print(p3.prod_id, p3.selling_price)
#print(p4.prod_id, p4.selling_price)

#p4.display = 10
#print(p4.prod_id, p4.selling_price)




