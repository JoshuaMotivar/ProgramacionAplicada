import math

tope_rango = 30
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(math.sqrt(n)) + 1):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    n += 1

ciclos_sin_break = 0
tope_rango = 30
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(math.sqrt(n)) + 1):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
tope_rango = 30
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(math.sqrt(n)) + 1):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se redujo a un ' + str(100 * ciclos_con_break / ciclos_sin_break) + '% del total de ciclos usando break')

tope_rango = 100
ciclos_sin_break = 0
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(math.sqrt(n)) + 1):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
n = 2
while n < tope_rango:
    primo = True
    for div in range(2, int(math.sqrt(n)) + 1):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se redujo a un ' + str(100 * ciclos_con_break / ciclos_sin_break) + '% del total de ciclos usando break')
