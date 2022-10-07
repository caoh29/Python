class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passanger(self, name):
        if self.open_seats > 0:
            self.passengers.append(name)
            return True
        else:
            return False

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(4)

people = ["Paula", "Camilo", "Chloe", "Liz", "Larry"]

for i in people:
    checkList = flight.add_passanger(i)
    if checkList:
        print("El pasajero fue asignado al vuelo")
    else:
        print("No hay asientos")