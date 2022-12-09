hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

y = (dura + mins)//60
hour_new = hour + y 

if hour_new<24:
    None
else:
    hour_new = hour_new-24

x = (dura + mins)%60

mins_new = x
print(f"{hour_new}:{mins_new}")