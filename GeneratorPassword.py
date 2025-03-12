import random

dic = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890+#$%&-*"
Contraseña = []
delimiter = ""

dic = list(dic)

x = 0
while x < (random.randint(8, 100)):
    x = x + 1
    Contraseña.append(random.choice(dic))

Contraseña = delimiter.join(Contraseña)

print("Tu contraseña es: ", Contraseña)