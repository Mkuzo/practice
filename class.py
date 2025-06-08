class FRUIT:
  color = "yellow"
  def _init_ (self,name,price):
    self.price = price
    self.name = name
  def about(self):
    print("I love ", self.color, self.name, "it is current price is ", self.spicy)
x = FRUIT("banana" , 200)
x.about()