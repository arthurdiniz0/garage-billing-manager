class Receipt:
    def __init__(self, date, customer, mechanic, vehicle, services, discount=0):
        self.date = date
        self.customer = customer
        self.mechanic = mechanic
        self.vehicle = vehicle
        self.services = services
        self.discount = discount
        self.taxes = 0
        self.total = 0
        self.finalAmount = 0

    def calculateTotal(self):
        total = sum(service.cost for service in self.services)
        return total

    def calculateTaxes(self):
        total = self.calculateTotal()
        taxes = total * 0.05
        return taxes

    def calculateFinalAmount(self):
        total = self.calculateTotal()
        taxes = self.calculateTaxes()
        final_amount = total + taxes - self.discount
        return final_amount
    
    def date(self):
        return self.date

    def date(self, date):
        self.date = date

    def getCustomer(self):
        return self.customer

    def setCustomer(self, customer):
        self.customer = customer

    def getMechanic(self):
        return self.mechanic

    def setMechanic(self, mechanic):
        self.mechanic = mechanic

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def getServices(self):
        return self.services

    def setServices(self, services):
        self.services = services

    def getTaxes(self):
        return self.taxes

    def setTaxes(self, taxes):
        self.taxes = taxes

    def getDiscount(self):
        return self.discount

    def setDiscount(self, discount):
        self.discount = discount

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total

    def getFinalAmount(self):
        return self.finalAmount

    def setFinalAmount(self, finalAmount):
        self.finalAmount = finalAmount

    def __str__(self):
            service_list = ''.join([f"{i + 1}. {service.getServiceType().name}\n" for i, service in enumerate(self.services)])
            total = self.calculateTotal()
            taxes = self.calculateTaxes()
            final_amount = self.calculateFinalAmount()
            return f"========RECEIPT========\n" \
                f"Customer Name: {self.customer.getFirstName()} {self.customer.getLastName()}\n" \
                f"Phone Number: {self.customer.getPhoneNumber()}\n" \
                f"Date: {self.date}\n" \
                f"Mechanic: {self.mechanic.getFirstName()} {self.mechanic.getLastName()}\n" \
                f"{self.vehicle}\n" \
                f"Services:\n{service_list}" \
                f"Taxes: {taxes:.2f}\n" \
                f"Total: {total:.2f}\n" \
                f"Discount: {self.discount:.2f}\n" \
                f"Final Amount: {final_amount:.2f}"