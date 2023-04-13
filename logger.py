class Logger:
    def __init__(self) -> None:
        self.transactional_count = 0
        self.daily_sales = 0
       

    def log_transaction(self, order, store_number):


        self.transactional_count += 1
        print(order)
        self.daily_sales += order.price
        print(store_number,order.dish_name, order.price )

