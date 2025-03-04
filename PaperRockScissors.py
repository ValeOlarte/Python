import random

print("Juguemos piedra, papel o tijera")
def game():

    #Variables
    list = [1, 2, 3]
    marcadorUser = 0
    marcadorComp = 0

    while True:

        number = random.choice(list)
        
    #Input de pregunta y numero correcto
        while True:
            print("----------------------------------------")
            print("piedra = 1, papel = 2 y tijera = 3")
            user = int(input("Selecciona tu numero: "))

            if 1 <= user <= 3:
                break
            else:
                print("Numero no valido")
                print("Intenta de nuevo")

    #Condicionales de puntos
        if user == number:
            print("Empate")
        elif user > number or (user == 1 and number == 3):
            print("Tu ganas")
            marcadorUser = marcadorUser + 1
        else:
            print("La comutadora gana")
            marcadorComp = marcadorComp + 1

    #Condicional de vistoria y fin del juego
        if marcadorComp == 3:
            print("----------------------------------------")
            print("La computadora gano 3 veces")
            print("Fin del juego")
            break

        if marcadorUser == 3:
            print("----------------------------------------")
            print("Tu ganaste 3 veces")
            print("Fin del juego")
            break

game()