from orderfactory import OrderFactory
from logger import Logger


class Franchise:
    def __init__(self) -> None:
        self.location_number = input(" Which loaction are you ordering from (1,2,or 3): \n")
        

    def place_order(self):
        order = OrderFactory()
        type = input(" What would you like to order?\n '1' for Pizza\n '2' for Pasta\n '3' for Salad:  ")  
        meal1 = order.create_order(type)
        print(meal1.dish_name, meal1.price)
        


    