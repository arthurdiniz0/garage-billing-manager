class Receipt:
    def __init__(self, customer, mechanic, vehicle, services, discount=0):
        self.customer = customer
        self.mechanic = mechanic
        self.vehicle = vehicle
        self.services = services
        self.discount = discount
        self.taxes = 0
        self.total = 0
        self.finalAmount = 0

    def calculateTotal(self):
        total = sum(service.price for service in self.services)
        return total

    def calculateTaxes(self):
        total = self.calculate_total()
        taxes = total * 0.05
        return taxes

    def calculate_final_amount(self):
        total = self.calculate_total()
        taxes = self.calculate_taxes()
        final_amount = total + taxes - self.discount
        return final_amount

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
            service_list = "\n".join([f"{i + 1}. {service}\n" for i, service in enumerate(self.services)])
            total = self.calculate_total()
            taxes = self.calculate_taxes()
            final_amount = self.calculate_final_amount()
            return f"Customer Name: {self.customer.getFirstName()} {self.customer.getLastName()}\n" \
                f"Cell Phone Number: {self.phone}\n" \
                f"Date: {self.date}\n" \
                f"Mechanic: {self.mechanic}\n" \
                f"Vehicle Type: {self.vehicleType}\n" \
                f"Vehicle Color: {self.vehicleColor}\n" \
                f"Vehicle ID: {self.vehicleId}\n\n" \
                f"Services\n{service_list}" \
                f"Taxes: {taxes:.2f}\n" \
                f"Total: {total:.2f}\n" \
                f"Discount: {self.discount:.2f}\n" \
                f"Final Amount: {final_amount:.2f}"