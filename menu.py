from os import system
from BaseDeDatos import *
from validarUsuario import *


# Se importa system, para limpiar la pantalla 'cls'
# y tambien se importa la BD en donde se encuentra la conexión y la mayoria de funciones a utilizar

# validarUsuario se encarga de confirmar si la cuenta ingresada esta en la BD y asignarle un perfil

#Por Falta de Buenas Practicas, al programa le falta en gran parte de validaciónes en los datos que se ingresan, tenga esto en consideración al utilizar el programa.

usuario=input(str("Ingrese su usuario:\n"))       #por ahora usaremos root

user=Usuario(usuario)
contraseña=input(str("Ingrese su contraseña:\n")) #inacap22 Personal / Ev1234 Server

if user.categoria=="jefe":
    db=DatabaseJEFE(user.cuenta,contraseña)
    
    while True:
        opcion=input('\nElija una opción:\n\
                \tIngresar Nuevo Empleado (I)\n\
                \tRevisar/Modificar cuenta Propia (V)\n\
                \tModificar cuenta de un usuario (M)\n\
                \tSuspender/Eliminar a un Trabajador (E)\n\
                \tListado de Trabajadores (L)\n\
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
        elif opcion=='l':
            db.listadoTrabajadores()
        elif opcion=='f':
            print('Fin')
            db.cerrarBD()
            break
        else:
            system('cls')
            print('Error de Opción')
        
             
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
            print("""
                    ░░░░░░░░░░░███████░░░░░░░░░░░
                    ░░░░░░░████░░░░░░░████░░░░░░░
                    ░░░░░██░░░░░░░░░░░░░░░██░░░░░
                    ░░░██░░░░░░░░░░░░░░░░░░░██░░░
                    ░░█░░░░░░░░░░░░░░░░░░░░░░░█░░
                    ░█░░████░░░░░░░░██████░░░░░█░
                    █░░█░░░██░░░░░░█░░░░███░░░░░█
                    █░█░░░░░░█░░░░░█░░░░░░░█░░░░█
                    █░█████████░░░░█████████░░░░█
                    █░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                    █░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                    █░░░████████████████████░░░░█
                    ░█░░░█▓▓▓▓▓▓▓▓█████▓▓▓█░░░░█░
                    ░█░░░░█▓▓▓▓▓██░░░░██▓██░░░░█░
                    ░░█░░░░██▓▓█░░░░░░░▒██░░░░█░░
                    ░░░██░░░░██░░░░░░▒██░░░░██░░░
                    ░░░░░██░░░░███████░░░░██░░░░░
                    ░░░░░░░███░░░░░░░░░███░░░░░░░
                    ░░░░░░░░░░█████████░░░░░░░░░░
                """)
        elif opcion=='f':
            print('Fin')
            db.cerrarBD()
            break
        else:
            system('cls')
            print('Error de Opción')
else:
    print("La categoria de usuario lo califica como Invasor, alejese de la computadora.")



