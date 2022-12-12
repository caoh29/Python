import sqlite3

def create_students_table():
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS Estudiantes (
            matricula TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            promedio REAL
        )
        '''
    )

    connection.commit()
    cursor.close()
    connection.close()



def insert_estudiante():
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO Estudiantes VALUES (:estudiante.matricula, :estudiante.nombre, :estudiante.apellido, :estudiante.promedio)', 
        {
            'estudiante.matricula': estudiante.matricula.get(),
            'estudiante.nombre': estudiante.nombre.get(),
            'estudiante.apellido': estudiante.apeliido.get(),
            'estudiante.promedio': estudiante.promedio.get()
        }
        )

    connection.commit()
    cursor.close()
    connection.close()



def update_promedio(matricula, promedio):
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute(
        'UPDATE Estudiantes SET promedio=? WHERE matricula=?', 
        (promedio, matricula)
        )

    connection.commit()
    cursor.close()
    connection.close()



def delete_estudiante(matricula):
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute(
        'DELETE from Estudiantes WHERE matricula=?', 
        (matricula,)
        )

    connection.commit()
    cursor.close()
    connection.close()



def select_student_matricula(matricula):
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Estudiantes WHERE matricula=?', (matricula,))

    datos =cursor.fetchall()

    cursor.close()
    connection.close()
    return datos



def select_student_nombre(nombre):
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Estudiantes WHERE nombre=?', (nombre,))

    datos = cursor.fetchall()

    cursor.close()
    connection.close()
    return datos



def select_student_apellido(apellido):
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Estudiantes WHERE apellido=?', (apellido,))

    datos = cursor.fetchall()

    cursor.close()
    connection.close()
    return datos



def select_all():
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Estudiantes')

    datos = cursor.fetchall()

    cursor.close()
    connection.close()
    return datos