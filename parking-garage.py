class parkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.remove(1)
        self.parkingSpaces.remove(1)
        print('Please take your ticket.')
        
    def payForParking(self):
        amount = input('Enter amount: $')
        if amount == '':
            print('Please pay your ticket.')
        else:
            print('Your ticket has been paid. You have 15 minutes to leave the garage.')
        self.currentTicket['paid'] = True
    
    def leaveGarage(self):
        if True in self.currentTicket.values():
            print(f'Thank you, have a nice day!')
        else:
            amount = input('Enter amount: $')
            if amount == '':
                print('Please pay your ticket.')
            else:
                print(f'Thank you, have a nice day!')
        self.parkingSpaces.append(1)
        self.tickets.append(1)
        

my_parkingGarage = parkingGarage([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], {})
print(my_parkingGarage.takeTicket())
print(my_parkingGarage.tickets)
print(my_parkingGarage.parkingSpaces)

print(my_parkingGarage.payForParking())
print(my_parkingGarage.currentTicket['paid'])

print(my_parkingGarage.leaveGarage())
print(my_parkingGarage.tickets)
print(my_parkingGarage.parkingSpaces)