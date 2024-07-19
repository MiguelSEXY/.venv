from os import system
while True:
        system('cls')
        tabla=input(\
        '¿Que tabla desea modificar?:\n\
        Datos de Usuario\t(1)\n\
        Datos Laborales\t\t(2)\n\
        Datos Personales\t(3)\n\
        Cancelar Operación\t(0)\n\
        =>\
        ')
        if tabla=="1":
                tabla="listadoTrabajadores"
                break
        elif tabla=="2":
                tabla="datosLaborales"
                break
        elif tabla=="3":
                tabla="datosPersonales"
                break
        elif tabla=="0":
                system('cls')
                break
print(tabla)