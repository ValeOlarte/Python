import random

dic = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890+#$%&-*"
dec = "+#$%&-*1234567890"
Contraseña = []
delimiter = ""

dic = list(dic)
dec = list(dec)

x = 0
while x < (random.randint(8, 100)):
    x = x + 1
    Contraseña.append(random.choice(dic))
    Contraseña.append(random.choice(dec))

Contraseña = delimiter.join(Contraseña)

print("Tu contraseña es: ", Contraseña)