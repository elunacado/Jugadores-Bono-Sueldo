import math
def Calculo():
    nombre = input("Cual es el nombre del jugador ")
    base = int(input("Cual es el sueldo base? "))
    bono_completo= int(input("cuanto es el bono completo "))
    bono_0= int(input("cuantos goles eran el MINIMO necesario para que el JUGADOR obtuviese la mitad el bono completa "))
    bono_1= int(input("cuantos goles METIO el JUGADOR "))
    bono_2= int(input("cuantos goles eran el MINIMO necesario para que el EQUIPO obtuviese la mitad el bono completa "))
    bono_3= int(input("cuantos goles METIO el EQUIPO "))


    result1 = (bono_1*100)/bono_0/2
    result2 = (bono_3*100)/bono_2/2

    TotalResult= result1+result2

    TotalBonus= math.floor((TotalResult*100)/bono_completo*100)*100

    Total=TotalBonus+base

    print("el bono total es: " + str(TotalBonus))
    print("y si el sueldo base es: "+ str(base))
    print("por lo tanto el sueldo total de "+ nombre + " " +str(Total))

Calculo()

OtraVez = input("Quieres calcular el sueldo de otro jugador? si/no")

if OtraVez=="si"or"Si"or"SI"or"sI":
    Calculo()
