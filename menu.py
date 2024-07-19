from os import system
from BaseDeDatos import *
from validarUsuario import *
from time import sleep

# system nos permitira realizar limpiezas de pantalla para no llenar la terminal.
# BaseDeDatos es la que contiene las clases Database, la cual contiene la conexión a la base de datos
# y contiene todas las funciones a las cuales se llaman desde el menu.
# validarUsuario es un pequeño script personal que confirma si el usuario ingresado esta en
# la lista de trabajadores con una cuenta en el sistema.

# Por Falta de Buenas Practicas, al programa le falta en gran cantidad de validaciónes 
# en los datos que se ingresan, tenga esto en consideración al utilizar el programa
# Nos Rehusamos a llamar a la aplicación una versión completa.

user=Usuario(input(str("Ingrese su usuario:\n=>")))
contraseña=input(str("Ingrese su contraseña:\n")) #inacap22 Personal / Ev1234 Server

# Dependiendo de la categoria del empleado se abrira 1 de las 3 clases de base de datos del modulo
# cada modulo tendra limitaciones en cuanto a las funciones que puede realizar, por ahora
# solo la categoria Jefe, tiene acceso a todas las funciones que ofrece el modulo.

###     Jefe        ###
if user.categoria=="jefe":
    db=DatabaseJEFE(user.cuenta,contraseña)
    
    while True:
        system('cls')
        opcion=input('\nElija una opción:\n\
                \tIngresar Nuevo Empleado (I)\n\
                \tRevisar/Modificar cuenta Propia (V)\n\
                \tModificar cuenta de un usuario (M)\n\
                \tSuspender/Eliminar a un Trabajador (E)\n\
                \tListado de Trabajadores (L)\n\
                \tFin(F)\n\
                \t=> ').lower()
        if opcion=='i':
            db.ingresarEmpleado()
        elif opcion=='v':
            db.verCuenta()
        elif opcion=='m':
            db.modificarCuentaUsuario()
        elif opcion=='e':
            db.eliminarCuentaUsuario()
        elif opcion=='l':
            db.listadoTrabajadores()
        elif opcion=='f':
            print('Fin')
            db.cerrarBD()
            break
        else:
            system('cls')
            print('Error de Opción')
            sleep(1.5)
        
###     Personal de RRHH        ###

elif user.categoria=="rrhh":
    db=DatabaseRRHH(user,contraseña)

    while True:
        opcion=input('\nElija una opción:\n\
                \tIngresar Nuevo Empleado (I)\n\
                \tRevisar/Modificar cuenta Propia (V)\n\
                \tModificar cuenta de un usuario (M)\n\
                \tSuspender a un Trabajador (E)\n\
                \tFin(F)\n\
                \t=> ').lower()
        system('cls')
        if opcion=='i':
            db.ingresarEmpleado()
        elif opcion=='v':
            db.verCuenta()
        elif opcion=='m':
            db.modificarCuentaUsuario()
        elif opcion=='e':
            db.eliminarCuentaUsuario()
        elif opcion=='f':
            print('Fin')
            db.cerrarBD()
            break
        else:
            system('cls')
            print('Error de Opción')

###     Empleado        ###
elif user.categoria=="empleado":
    db=DatabaseEmpleado(user,contraseña)

    while True:
        opcion=input('\nElija una opción:\n\
                \tRevisar/Modificar cuenta Propia (V)\n\
                \tFin(F)\n\
                \t=> ').lower()
        system('cls')
        if opcion=='v':
            db.verCuenta()
        elif opcion!="v" and opcion !="f":
            sleep(0.5)
            print("░░░░░░░░░░░███████░░░░░░░░░░░")
            sleep(0.2)
            print("░░░░░░░████░░░░░░░████░░░░░░░")
            sleep(0.2)
            print("░░░░░██░░░░░░░░░░░░░░░██░░░░░")
            sleep(0.2)
            print("░░░██░░░░░░░░░░░░░░░░░░░██░░░")
            sleep(0.2)
            print("░░█░░░░░░░░░░░░░░░░░░░░░░░█░░")
            sleep(0.2)
            print("░█░░████░░░░░░░░██████░░░░░█░")
            sleep(0.2)
            print("█░░█░░░██░░░░░░█░░░░███░░░░░█")
            sleep(0.2)
            print("█░█░░░░░░█░░░░░█░░░░░░░█░░░░█")
            sleep(0.2)
            print("█░█████████░░░░█████████░░░░█")
            sleep(0.2)
            print("█░░░░░░░░░░░░░░░░░░░░░░░░░░░█")
            sleep(0.2)
            print("█░░░░░░░░░░░░░░░░░░░░░░░░░░░█")
            sleep(0.2)
            print("█░░░████████████████████░░░░█")
            sleep(0.2)
            print("░█░░░█▓▓▓▓▓▓▓▓█████▓▓▓█░░░░█░")
            sleep(0.2)
            print("░█░░░░█▓▓▓▓▓██░░░░██▓██░░░░█░")                
            sleep(0.2)
            print("░░█░░░░██▓▓█░░░░░░░▒██░░░░█░░")
            sleep(0.2)
            print("░░░██░░░░██░░░░░░▒██░░░░██░░░")
            sleep(0.2)
            print("░░░░░██░░░░███████░░░░██░░░░░")
            sleep(0.2)
            print("░░░░░░░███░░░░░░░░░███░░░░░░░")
            sleep(0.2)
            print("░░░░░░░░░░█████████░░░░░░░░░░")
            sleep(2)
            system('cls')
        elif opcion=='f':
            print('Fin')
            db.cerrarBD()
            break
        else:
            system('cls')
            print('Error de Opción')
else:
    # En caso de que se haya ingresado un usuario no verificado en la validación, se le
    # entrega el siguiente mensaje:
    system('cls')
    print("La categoria de usuario lo califica como Invasor, alejese de la computadora.")



