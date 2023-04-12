from order import Order

class Logger:
    def __init__(self) -> None:
        self.transactional_count = 0
        self.daily_sales = 0

    def log_transaction(self):
        self.order = Order()