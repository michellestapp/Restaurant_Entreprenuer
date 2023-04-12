from order import Order

class Logger:
    def __init__(self) -> None:
        self.transactional_count = 0
        self.daily_sales = 0

    def log_transaction(self, Order, store_number):
        self.order = Order()
        print(f'You ordered a {self.order.dish_name} which costs {self.order.price} from store location {store_number}')
        self.transactional_count += 1
        self.daily_sales += self.order.price

# my_order = Pasta()
# log_transaction(my_order, 2505)