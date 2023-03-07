class Customer:
    def __init__(self, customerID, firstName, lastName, phoneNumber, address):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.address = address

    def getCustomerID(self):
        return self.customerID
    
    def setCustomerID(self, customerID):
        self.customerID = customerID

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __str__(self):
        return f"Customer Name: {self.firstName} {self.lastName}\nCell Phone Number: {self.phoneNumber}\nCustomer ID: {self.customerID}\nAddress: {self.address}"