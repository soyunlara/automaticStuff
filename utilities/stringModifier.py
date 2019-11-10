#Se puede mejorar enormemente
#Agregar modificacion a cadena modificada.

last_aux = 1
change_this = ''
with_this = ''
pls = ''
while True:
    if last_aux == 1 or last_aux == "1":
        change_this = input('******************************************\nCadena a editar -> ')
        with_this = input('Cambia esto: ')
        pls = input('Por esto: ')
        myString = change_this
        print('\nCadena modificada\n'+myString.replace(with_this,pls)+'\n')
        last_aux = input('*** Opciones ***\n1 - Cambiar cadena original\n2 - Cambiar parte a modificar\n0 - Salir\nOpcion: ')
    elif last_aux == 2 or last_aux == "2":
        pls = input('******************************************\nPor esto: ')
        myString = change_this
        print('\nCadena modificada\n'+myString.replace(with_this,pls)+'\n')
        last_aux = input('*** Opciones ***\n1 - Cambiar cadena original\n2 - Cambiar parte a modificar\n0 - Salir\nOpcion: ')
    elif last_aux == 0 or  last_aux == "0":
        break

