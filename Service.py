from enum import Enum

class ServiceType(Enum):
    DIAGNOSTICS = 1
    OIL_REPLACEMENT = 2
    OIL_FILTER_PARTS = 3
    TIRE_REPLACEMENT = 4
    TIRE = 5

class Service:
    def __init__(self, serviceID, serviceType, vehicle, customer, mechanic, amount):
        self.serviceID = serviceID
        self.serviceType = serviceType
        self.vehicle = vehicle
        self.customer = customer
        self.mechanic = mechanic
        self.amount = amount
        
        prices = {1:15, 2:120, 3:35, 4:50, 5:80} # dictionary correlating service types and prices
        self.cost = prices[self.serviceType.value] * amount



    def getServiceID(self):
        return self.serviceID

    def setServiceID(self, serviceID):
        self.serviceID = serviceID

    def getServiceType(self):
        return self.serviceType

    def setServiceType(self, serviceType):
        self.serviceType = serviceType

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def getCustomer(self):
        return self.customer

    def setCustomer(self, customer):
        self.customer = customer

    def getMechanic(self):
        return self.mechanic

    def setMechanic(self, mechanic):
        self.mechanic = mechanic

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.serviceType.name}.\nCustomer: {self.customer.getFirstName()} {self.customer.getLastName()}\nVehicle: {self.vehicle}\nMechanic: {self.mechanic.getFirstName()} {self.mechanic.getLastName()}\nAmount: {self.amount}\nCost: {self.cost}\n"
    

#srvc = Service(serviceID=1, serviceType=ServiceType.DIAGNOSTICS, customer='Arthur', mechanic='Cleber', amount=3)
#print(srvc)