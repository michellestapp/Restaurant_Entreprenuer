from orderfactory import OrderFactory
from logger import Logger


class Franchise:
    def __init__(self):
        self.location_number = int(input(" Which location are you ordering from (1,2,or 3): \n"))
    
        

    def place_order(self):
        orderfactory = OrderFactory()
        log = Logger()

    

        self.type = int(input(" What would you like to order?\n '1' for Pizza\n '2' for Pasta\n '3' for Salad:  ")) 
        meal1 = orderfactory.create_order(self.type)
        print(meal1.dish_name , meal1.price)
        print(f'You ordered a {meal1.dish_name} which costs ${meal1.price} from store location {self.location_number}')
        
        log.log_transaction(meal1,self.location_number)
        


    