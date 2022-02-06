# classmethod and staticmethod
    # classmethod geen instantie van nodig om die aan te spreken
    # staticmethod is eigenlijk een aparte functie die in de klasse leeft

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return  f"{store.name}, total stock price: {store.stock_price()}"


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard",160)
Store.franchise(store)
Store.franchise(store2)

Store.store_details(store2)