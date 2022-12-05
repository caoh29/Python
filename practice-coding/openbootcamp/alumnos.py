class Alumno:
    __nombre = ""
    __nota = 0

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNota(self):
        return self.__nota
    
    def setNota(self, nota):
        self.__nota = nota

    def isAprobado(self):
        if self.__nota >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"

a1 = Alumno()
a1.setNombre("Camilo")
a1.setNota(5.0)

a2 = Alumno()
a2.setNombre("Larry")
a2.setNota(2.7)

print(f"El Alumno {a1.getNombre()} con la nota {a1.getNota()} ha {a1.isAprobado()}")
print(f"El Alumno {a2.getNombre()} con la nota {a2.getNota()} ha {a2.isAprobado()}")