from orderfactory import OrderFactory
from franchise import Franchise

class Simulation:
    def __init__(self) -> None:
        pass

    def run_simulation(self):
        meal  = Franchise(2)
        meal.place_order()        
        meal.place_order()

