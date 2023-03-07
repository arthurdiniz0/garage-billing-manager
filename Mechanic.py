class Mechanic:
    def __init__(self, firstName, lastName, mechanicID):
        self.firstName = firstName
        self.lastName = lastName
        self.mechanicId = mechanicID

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getMechanicID(self):
        return self.mechanicId

    def setMechanicID(self, mechanicID):
        self.mechanicId = mechanicID

    def __str__(self):
        return f"Mechanic Name: {self.firstName} {self.lastName}\nMechanic ID: {self.mechanicId}\n"
