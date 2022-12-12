notas_num = int(input('Cuantas notas sacará durante el periodo: '))

notas =[]
for i in range(notas_num):
    notas.append(f'nota{i+1} REAL,')

print(notas)