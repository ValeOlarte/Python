a = 0
b = 101
userNumber = 0

def guessNumber (a, b):
    
    intentos = 0
    print("Este es un programa en el cual pones a adivinar a la maquina el numero elegido ente 1 y 100")
    
    while True:
        
        userNumber = int(input("Escribe tu numero: "))
        if 100 >= userNumber >= 1:
            break
        else:
            None
    
    while True:
        
        intentos = intentos + 1
        randomNumber = round((a + b)/2)
        
        if randomNumber == userNumber:
            print ("el numero fue: ")
            print (randomNumber)
            print ("-La computadora adivino-")
            print ("adivino en: ", intentos)
            print(    )
            break
            
        if randomNumber > userNumber:
            b = randomNumber
            print ("el numero fue: ")
            print (randomNumber)
            print ("-seguir adivinando-")
            print(    )
        
        if randomNumber < userNumber:
            a = randomNumber
            print ("el numero fue: ")
            print (randomNumber)
            print ("-seguir adivinando-")        
            print(    )
            
guessNumber(a, b)