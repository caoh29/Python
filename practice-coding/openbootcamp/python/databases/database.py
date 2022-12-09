import sqlite3
from estudiantes import Estudiante

connection = sqlite3.connect('universidad.db')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Estudiantes')

cursor.execute(
    ''' 
    CREATE TABLE Estudiantes (
        matricula TEXT,
        nombre TEXT,
        apellido TEXT,
        promedio REAL
    )
    '''
)

est_1 = Estudiante('0001', 'Camilo', 'Ordoñez', 4.0)
est_2 = Estudiante('0002', 'Paula', 'Manrique', 4.2)
est_3 = Estudiante('0003', 'Ricard', 'Ordoñez', 3.2)
est_4 = Estudiante('0004', 'Edilma', 'Herrera', 4.0)
est_5 = Estudiante('0005', 'Aura', 'Uribe', 3.5)

cursor.execute(
    'INSERT INTO Estudiantes VALUES (?, ?, ?, ?)', (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio)
    )


connection.commit()


cursor.execute('SELECT * FROM Estudiantes')
estudiantes = cursor.fetchall()


print(estudiantes)


cursor.close()
connection.close()