class Logger:
    def __init__(self) -> None:
        self.transactional_count = 0
        self.daily_sales = 0
       

    def log_transaction(self, order, store_number):


        self.transactional_count += 1
    
        self.daily_sales += order.price

        document = open('log.txt','a')
        document.write(f"TXT#{self.transactional_count}: {order.dish_name} at location {store_number} = ${order.price}. Total Sales for all locations = ${self.daily_sales}\n")
        document.close()
        print(store_number,order.dish_name, order.price )

