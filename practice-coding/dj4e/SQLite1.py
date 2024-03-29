import sqlite3
#Nos conectamos a la Base de Datos
connection = sqlite3.connect('emaildb.sqlite')

#Creamos un cursor que nos servira como navegador dentro  de la base de datos
cursor = connection.cursor()

#En caso de que la tabla ya exista, este comando impide que crashee el codigo :v
cursor.execute('DROP TABLE IF EXISTS Counts')

#Crea una tabla llamada Counts con los parametros email y count
cursor.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

#Obtiene un nombre de archivo
file_name = input('Enter file name: ')

#Si la longitud del nombre del archivo es menor que uno, tome el siguiente nombre como predeterminado
if (len(file_name) < 1):
    #Nombre de archivo igual a mbox-short.txt
    file_name = 'emails.txt'
    
#Creamos el stream del archivo llamado file_handler
file_handler = open(file_name)

#Por cada linea que se encuentra en file_handler, haga lo siguiente:
for line in file_handler:
    #Si la linea que se esta leyendo NO inicia con "From: ", No la lea
    if not line.startswith('From: '): continue
    #Se para las palabras de acuerdo a los espacio vacios entre ellas
    pieces = line.split()
    #Tomamos el email que se encuentra en la primer linea del archivo de texto
    email = pieces[1]
    #usamos SQL por medio del metodo execute: Seleccionamos el parámetros "count" de la base de datos "Count" en donde el email vale ?, 
    #en donde ? es un placeholder que sera reemplazado por (email,), esto con el fin de evitar SQL INJECTION
    cursor.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    #for the first item that match the SQL, grab the item and assign it to row
    row = cursor.fetchone()
    # Si la variable row esta vacia, haga lo siguiente:
    if row is None:
        #Inserte en la tabla Count los parametros email y count y asigne los valores (email,) en lugar de ? y count igual a 1
        cursor.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    #Si no cumple, haga:
    else:
        #Actualice la tabla Counts y sumele 1 a el parametro Count de acuerdo a su email
        # Se recomienda usar UPDATE es mejor que leer y luego añadir 
        cursor.execute('UPDATE Counts SET  count = count + 1 WHERE email = ?', (email,))
    #Haga un commit de la conexion con la base de datos
    connection.commit()

#se crea un objeto con comando SQL en donde seleccionan los parametros email y count de la tabla Counts ordenada por count 
#en orden descendente y con limite de 10
sql_string = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#Por cada fila de la tabla que cumpla con lo especificado en la linea 52, haga lo sieguiente:
for row in cursor.execute(sql_string):
    #imprima el email (row[0]) y count (row[1])
    print(str(row[0]), row[1])

#cierre el handler
cursor.close()