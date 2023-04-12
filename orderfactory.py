from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def create_order(self,type, price):
        type = input(" What would you like to order? Pizza, Pasta, or Salad?")
        if type == "Pizza":
            return Pizza()
        elif type == "Pasta":
            return Pasta()
        else:
            return Salad()
        


