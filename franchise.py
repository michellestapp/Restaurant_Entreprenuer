from orderfactory import OrderFactory
from logger import log
class Franchise:
    def __init__(self):
        self.location_number = int

    def place_order(self):
        orderfactory = OrderFactory()
        print(f' Welcome to the Pizza Emporium!!  We have three locations: \n')

        self.location_number = int(input(" Which location are you ordering from:\n Press '1' for the Redondo store\n Press '2' for the Broadmoor store\n Press '3' for the Ballwin store: \n"))
        self.type = int(input("\n What would you like to order?\n '1' for Pizza\n '2' for Pasta\n '3' for Salad: \n ")) 
        meal = orderfactory.create_order(self.type)
        print(f'You ordered a {meal.dish_name} which costs ${meal.price} from store location {self.location_number}\n')
        
        log.log_transaction(meal,self.location_number)
        


    