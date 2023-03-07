class Mechanic:
    def __init__(self, mechanicID, firstName, lastName, phoneNumber, address):
        self.firstName = firstName
        self.lastName = lastName
        self.mechanicId = mechanicID
        self.phoneNumber = phoneNumber
        self.address = address

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

    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.PhoneNumber = phoneNumber
    
    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address



    def __str__(self):
        return f"Mechanic Name: {self.firstName} {self.lastName}\nMechanic ID: {self.mechanicId}\nPhone Number: {self.phoneNumber}\nAddress: {self.address}"
