import webbrowser
import schedule
import time

def abrir_google():
    url = "https://ioma.gba.gob.ar"
    webbrowser.open(url)

# Programar la tarea de abrir Google cada 15 minutos
schedule.every(1).minutes.do(abrir_google)

# Ejecutar el bucle principal
while True:
    schedule.run_pending()
    time.sleep(1)



mi_lista = [1,2,3,4,5]
mi_lista2 = [1,'auto',5,'anacleto']



del mi_lista2[2]

print(mi_lista2)

