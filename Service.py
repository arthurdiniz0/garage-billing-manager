class Service:
    def __init__(self, serviceName, price):
        self.serviceName = serviceName
        self.price = price

    def get_serviceName(self):
        return self.serviceName

    def set_serviceName(self, serviceName):
        self.serviceName = serviceName

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"{self.serviceName}. Price: {self.price}\n"