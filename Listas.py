#Declarar lista con tamaño 10
#Definir Valores enteros
#Elevar a la quinta potencia los numeros impares
#Multiplicar por el num anterior el numero par
#Imprimir resultados

lista = [0]*10

for i in range(10):

    lista[i] = int(input("Ingrese un numero entero: "))

for i in range(10):

    if lista[i] % 2 != 0:

        print(f"El numero {lista[i]} es impar.")

        lista[i] = lista[i] ** 5

        print(f"elevado a la quinta potencia es {lista[i]}.")
        print("----" * 20)

    else:

        print(f"El numero {lista[i]} es par.")

        if i == 0:

            lista[i] = lista[i] * (-1)

        else:

            lista[i] = lista[i] * lista[i-1]

        print(f"multiplicado por el numero anterior es {lista[i]}.")
        print("----" * 20)
