class Vehicle:
    def __init__(self, make, model, color, year, vehicleID):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.vehicleId = vehicleID

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
    
    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def getVehicleID(self):
        return self.vehicleId

    def setVehicleID(self, vehicleID):
        self.vehicleId = vehicleID

    def __str__(self):
        return f"Vehicle Type: {self.make} {self.model}\nVehicle Color: {self.color}\nVehicle Year: {self.year}\nVehicle ID: {self.vehicleId}"