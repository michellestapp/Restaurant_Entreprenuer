from orderfactory import OrderFactory
from logger import Logger
from order import Order


class Franchise:
    def __init__(self) -> None:
        self.location_number = input(" Which location are you ordering from (1,2,or 3): \n")
        return self.location_number
        

    def place_order(self):
        order = OrderFactory()
        log = Logger()

        self.type = input(" What would you like to order?\n '1' for Pizza\n '2' for Pasta\n '3' for Salad:  ") 
        meal1 = order.create_order(self.type)
        print(meal1.dish_name, meal1.price)
        log.log_transaction(self.type,self.location_number)
        


    