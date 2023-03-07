class Vehicle:
    def __init__(self, make, model, color, vehicleID):
        self.make = make
        self.model = model
        self.color = color
        self.vehicleId = vehicleID

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_vehicleID(self):
        return self.vehicleId

    def set_vehicleID(self, vehicleID):
        self.vehicleId = vehicleID

    def __str__(self):
        return f"Vehicle Type: {self.make} {self.model} ({self.vehicleId})\nVehicle Color: {self.color}\n"