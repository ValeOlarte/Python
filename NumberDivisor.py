x = 9.8
a = 0
def calcularDivisores (a):

    a = int(input("Numero: "))
    
    numbers = []
    b = 0
    
    while a:
        b = b + 1
        numbers.append(b)
        if b == a:
            break
    
    divisores = []
    
    for i in numbers:
        d = (a / i)
        entero = d - int(d)
        if entero == 0:
            divisores.append(i)
        else:
            None

    print(divisores)

calcularDivisores (a)