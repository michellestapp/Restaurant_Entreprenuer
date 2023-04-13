from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:
    def create_order(self,type=int):
         
    
        if type == 1:
            return Pizza()
        elif type == 2:
            return Pasta()
        elif type == 3:
            return Salad()
        

        


