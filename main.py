from Mechanic import Mechanic
from Receipt import Receipt
from Service import Service, ServiceType
from Vehicle import Vehicle
from Customer import Customer

customer1 = Customer('1001','Arthur','Souza','+971 58 533 1710','The Myriad Dubai G524')
vehicle1 = Vehicle('Ford', 'Civic Sedan','White',2023,'1111')
mechanic1 = Mechanic(12, 'Cleber', 'Gonçalves', '+971 53 533 1094', 'Al Barsha Residencial Dubai')

service1 = Service('12345', ServiceType.OIL_REPLACEMENT, vehicle1, customer1, mechanic1, 1)
service2 = Service('12345', ServiceType.TIRE_REPLACEMENT, vehicle1, customer1, mechanic1, 2)

receipt1 = Receipt('25-03-2023',customer1, mechanic1, vehicle1, [service1, service2], discount=10)
print(receipt1)