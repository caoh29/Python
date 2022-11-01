import urllib.error, urllib.parse, urllib.request

#Se crea una request a la url ingresada y se asigna el stream a la variable file_handler
file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}

#Por cada linea en file_handler, se hace:
for line in file_handler:
    #Se decodifica la linea ya que esta en estado binario y se omiten los espacios blancos entre ellas
    line = line.decode().strip()
    #Se separa cada linea de acuerdo a los espacios vacios entre cada palabra y se asigna a la variable words la cual es un array
    words = line.split()
    #por cada palabra en la linea, haga:
    for word in words:
        # se añade word como llave en el diccionario counts y se le asigna el valor de 0 a dicha palabra, y cada vez que la vea nuevamente se suma 1 al valor.
        counts[word] = counts.get(word, 0) + 1
    #se imprime la linea
    print(line)

print(counts)