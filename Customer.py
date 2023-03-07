class Customer:
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, firstName):
        self.firstName = firstName

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_phone_number(self):
        return self.phoneNumber

    def set_phone_number(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"Customer Name: {self.firstName} {self.lastName}\nCell Phone Number: {self.phoneNumber}\n"