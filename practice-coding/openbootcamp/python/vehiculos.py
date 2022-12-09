class Vehiculo:
    __color = ""
    __ruedas = 0
    __puertas = 0

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def getRuedas(self):
        return self.__ruedas
    
    def setRuedas(self, ruedas):
        self.__ruedas = ruedas
    
    def getPuertas(self):
        return self.__puertas
    
    def setPuertas(self, puertas):
        self.__puertas = puertas

class Coche(Vehiculo):
    __velocidad = 0
    __cilindrada = 0
    

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def getCilindrada(self):
        return self.__cilindrada
    
    def setCilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
    

c = Coche()
c.setColor("gris")
c.setCilindrada(2000)
c.setPuertas(5)
c.setRuedas(4)
c.setVelocidad(200)

print("Color:",c.getColor(),"Cilindrada:",c.getCilindrada(),"Puertas:",c.getPuertas(),"Ruedas:",c.getRuedas(),"Velocidad:",c.getVelocidad())