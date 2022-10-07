class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
            

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(4)

people = ["Paula", "Camilo", "Chloe", "Liz", "Larry"]

for i in people:
    checkList = flight.add_passanger(i)
    if checkList:
        print(f"El pasajero {i} fue asignado al vuelo")
    else:
        print(f"No hay asiento para {i}")