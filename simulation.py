from orderfactory import OrderFactory
from franchise import Franchise

class Simulation:
    def __init__(self) -> None:
        pass

    def run_simulation(self):
        meal1 = Franchise()
        meal2 = Franchise()
        meal1.place_order()
        meal2.place_order()

