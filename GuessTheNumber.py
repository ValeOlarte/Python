import random
import time

randomNumber = random.randint(1, 10)

def guessNumber ():
    
    print("Adivina el numero de entre 1 a 10")
    
    while True:
        
        time.sleep(1)
        userNumber = int(input("Escribe tu numero: "))
        
        if userNumber > 10 or userNumber < 1:
            
            time.sleep(0.5)
            print("-------------------------------------------")
            print("😒😒El numero debe ser entre 1 y 10😒😒")
            print("Intenta de nuevo🔁")
            print("-------------------------------------------")
            
        elif userNumber > randomNumber:
            
            time.sleep(0.5)
            print("----------------------")
            print("El numero es mas bajo🔽")
            print("Intenta de nuevo🔁")
            print("----------------------")
            
        elif userNumber < randomNumber:
            
            time.sleep(0.5)
            print("----------------------")
            print("El numero es mas alto🔼")
            print("Intenta de nuevo🔁")
            print("----------------------")
        
        if userNumber == randomNumber:
            
            time.sleep(0.5)
            print("----------------------")
            print("Adivinaste el numero")
            print("🎉🎉Ganaste🎉🎉")
            break
        
guessNumber()