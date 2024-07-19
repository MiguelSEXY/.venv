import mysql.connector
from os import system
import datetime
from time import sleep
# mysql.connector realizara la conexión con la base de datos y se encargara
# de ejecutar las instrucciones que realizaremos para MySQL
# system nos permitira realizar limpiezas de pantalla para no llenar la terminal
# datetime cumple una funcion especifica en uno de los campos de fecha
# sleep nos permitira realizar pequeñas pausas durante la ejecución del código 



###         Funciones de Jefe           ###
class DatabaseJEFE:
    # al instanciar 
    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        # Establecemos la conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host='localhost',       # Dirección del servidor / WinServer:'192.168.1.7'
            user=usuario,             # Usuario de la base de datos
            database='nomina',        # Nombre de la base de datos
            password=contraseña       # Contraseña de la base de datos
        )
        # Creamos un cursor para ejecutar queries
        self.cursor = self.conexion.cursor(buffered=True)

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()
    
    def ingresarEmpleado(self):
        #Es necesario que la BD cuente con 1 rut de Personal de RRHH para el ingreso de datos
        #Para facilitar el proceso se ha designado 1 Rut para Personal de RRHH
        RutPersonalRRHH='20200200-2'
        system('cls')
        print('Datos de Cuenta, Nuevo Empleado:\n')
        #Se Procede a rellenar los datos necesarios para completar el formulario.
        #Es necesario iniciar por la taba de ListadoTrabajadores, para rellenar el resto de datos.

        ###         Datos de Cuenta            ###
        rutListado=str(input('Ingrese el Rut del Nuevo Empleado:\n=>'))
        usuario=str(input('Ingrese el nombre de Usuario que tendra la cuenta del trabajador:\n=>'))
        contraseña=str(input('Ingrese la contraseña de la cuenta del trabajador:\n=>'))
        while True:
            system('cls')
            print("Rut:",rutListado,"\nUsuario:",usuario)
            perfil=int(input(\
                            'Tipos de Perfil:\
                            \nEmpleado:\t1\
                            \nPersonal_RRHH:\t2\
                            \n=>'))
            if perfil==1:
                perfilPersonal="empleado"
                break
            elif perfil==2:
                perfilPersonal="personal_rrhh"
                break
            else:
                system('cls')
                print('Opción Invalida')
        #con los datos ya preparados, se arma la instrucción
        sql1="insert into listadoTrabajadores (rutListado,rutPersonalRRHH,usuario,contraseña,perfilCuenta) values (%s, %s, %s, %s, %s)"
        try:
            #se ejecuta la instruccion, si esta llega correctamente se actualiza con el commit.
            self.cursor.execute(sql1, (rutListado,RutPersonalRRHH,usuario,contraseña,perfilPersonal))            
            self.conexion.commit()
        except Exception as err:
            #En caso de que ocurra un error, se realizara un rollback de emergencia y se informara el error ocurrido.
            self.conexion.rollback()
            print(err)

        ###         Datos Personales        ###

        system('cls')
        print('Datos Personales:\nRut:',rutListado,'\n')
        #rutPer corresponde al mismo trabajador del rutListado, la variable apunta al mismo dato.
        rutPer=rutListado
        nombrePer=str(input('Ingrese el nombre del Trabajador:\n=>'))
        while True:
            sexoPer=str(input('Ingrese su Sexo:\nH=Hombre\nM=Mujer\nO=Otro\n=>')).lower()
            if sexoPer=='h':
                sexoPer="Hombre"
                break
            elif sexoPer=='m':
                sexoPer="Mujer"
                break
            elif sexoPer=="o":
                sexoPer="Otro"
                break
            else:
                print("Error al ingresar su sexo")

        direccionPer=str(input('Ingrese la dirección del trabajador:\n=>'))
        telefonoPer=str(input('Ingrese el telefono del trabajador:\n=>'))

        sql2="insert into datosPersonales (rutPer,rutListado, nombrePer,sexoPer, direccionPer, telefonoPer) values (%s, %s, %s, %s, %s,%s)"
        try:
            self.cursor.execute(sql2, (rutPer,rutListado,nombrePer,sexoPer,direccionPer, telefonoPer))            
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Datos Laborales         ###

        system('cls')
        print('Datos Laborales:\n')
        iDTrabajador=int(input('Ingrese el ID (númerico) del trabajador:\n=>'))
        departamento=str(input('Ingrese el departamento al que pertenece:\n=>'))
        area=str(input('Ingrese el Área del trabajador:\n=>'))
        cargo=str(input('Ingrese el Cargo del trabajador:\n=>'))
        print('Fecha de Ingreso:\n=>')
        fecha = input('Ingrese la fecha de ingreso (dd/mm/aaaa):\n=>')
        fechaIngreso=datetime.datetime.strptime(fecha,"%d/%m/%Y")

        sql3="insert into DatosLaborales (IdTrabajador,rutListado, Departamento,Area, Cargo, FechaIngreso) values (%s, %s, %s, %s, %s,%s)"
        try:
            
            self.cursor.execute(sql3, (iDTrabajador, rutListado,departamento,area ,cargo, fechaIngreso))            
            self.conexion.commit()
            system('cls')
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Contacto de Emergencia       ###

        # se da libertad de ingresar varios contactos o ninguno, pero por ahora el programa
        # necesita que exista por lo menos 1 ingreso
        while True:
            opcion=str(input('¿Desea agregar un contacto de Emergencia? (s/n):\n=>')).lower()
            if opcion=='s':
                system('cls')
                print('Contacto De Emergencia:\n=>')

                rutEmer=str(input('Ingrese el rut del contacto de Emergencia:\n=>'))
                nombreEmer=str(input('Ingrese el nombre del Contacto de Emergencia:\n=>'))
                numPrioridad=int(input('Ingrese la prioridad del Contacto de Emergencia (de forma númerica):\n=>'))
                telefonoEmer=str(input('Ingrese el telefono para el Contacto de Emergencia:\n=>'))
                relacionEmer=str(input('Ingrese la relación con el Contacto de Emergencia:\n=>'))

                sql4="insert into contactosEmergencia (rutEmer, rutListado, NombreEmer,\
                        numPrioridad,TelefonoEmer, RelacionEmer) values (%s, %s, %s, %s, %s,%s)"
                
                try:
                    self.cursor.execute(sql4, (rutEmer, rutListado,nombreEmer,numPrioridad,telefonoEmer ,relacionEmer))            
                    self.conexion.commit()
                    print('Contacto Ingresado Exitosamente')
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                system('cls')
                break
        ###         Carga Familiar    ###

        # se da libertad de ingresar varias cargas o ninguna, pero por ahora el programa
        # necesita que exista por lo menos 1 ingreso
        while True:
            print('Carga Familiar:\n')
            opcion=str(input('¿Desea ingresar una carga familiar? (s/n)\n=>')).lower()
            if opcion=="s":
                rutCarga=str(input('Ingrese el Rut de la Carga Familiar:\n=>'))
                nombreCarga=str(input('Ingrese el nombre de la Carga Familiar:\n=>'))
                while True:
                    sexoCarga=str(input('Ingrese el sexo de su carga:\nH=Hombre\nM=Mujer\nO=Otro\n=>')).lower()
                    if sexoCarga=='h':
                        sexoCarga="Hombre"
                        break
                    elif sexoCarga=='m':
                        sexoCarga="Mujer"
                        break
                    elif sexoCarga=="o":
                        sexoCarga="Otro"
                        break
                    else:
                        print("Error al ingresar su sexo")

                parentescoCarga=str(input('Ingrese el parentesco de la Carga Familiar:\n=>'))

                sql5="insert into CargasFamiliares (rutCarga, rutListado, nombreCarga, sexoCarga, parentescoCarga) \
                        values (%s, %s, %s, %s, %s)"
                try:
                    self.cursor.execute(sql5,(rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga))
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                break

    def verCuenta(self):
        system('cls')

    # se realiza una consulta dependiendo de la tabla que el usuario quiera visualizar
    # posteriormente se le dara la opción de modificar datos de la tabla elegida.
        while True:
            system('cls')
            tabla=input(\
            '¿Que datos desea observar?:\n\
            Datos Personales:\t\t(1)\n\
            Cargas Familiares:\t\t(2)\n\
            Contactos de Emergencia:\t(3)\n\
            =>\
            ')
            if tabla=="1":
                tabla="datosPersonales"
                break
            elif tabla=="2":
                tabla="cargasFamiliares"
                break
            elif tabla=="3":
                tabla="contactosEmergencia"
                break
        if tabla=="datosPersonales":
            sql1='select rutPer,nombrePer,sexoPer,direccionPer,telefonoPer,l.rutListado from\
                  datosPersonales d, listadoTrabajadores l \
                  where d.rutListado=l.rutListado \
                  and l.usuario="'+self.usuario+'"'
        #la consulta se especifica utilizando el nombre de usuario como referencia en la busqueda
        elif tabla=='cargasFamiliares':
            sql1='select rutCarga,nombreCarga,sexoCarga,parentescoCarga,l.rutListado from\
                cargasFamiliares c, listadoTrabajadores l \
                where c.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        elif tabla=='contactosEmergencia':
            sql1='select rutEmer,nombreEmer,numPrioridad,telefonoEmer,relacionEmer,l.rutListado from\
                contactosEmergencia e, listadoTrabajadores l \
                where e.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        try:
            self.cursor.execute(sql1)
            datos=self.cursor.fetchone()
            rutListado=datos[-1]
            if tabla=='datosPersonales':
                while datos is not None:
                    # system('cls')
                    print('\
                            Rut:\t',datos[0],'\n\
                            Nombre:',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Dirección:',datos[3],'\n\
                            Telefono:',datos[4],'\n')
                    datos=self.cursor.fetchone()
                    while True:
                        modi=input('¿Desea Modificar alguno de los datos? (s/n)\n=>').lower()
                        if modi=='s':
                            while True:
                                system('cls')
                                campoMod=input('Ingrese el campo que desea modificar:\n\
                                    Nombre\t(1)\n\
                                    Sexo:\t(2)\n\
                                    Direccion:\t(3)\n\
                                    Telefono\t(4)\n=>')
                                if campoMod=="1":
                                    campoMod="nombrePer"
                                    break
                                elif campoMod=="2":
                                    campoMod="sexoPer"
                                    break
                                elif campoMod=="3":
                                    campoMod="direccionPer"
                                    break
                                elif campoMod=="4":
                                    campoMod="telefonoPer"
                                    break
                            nuevoValor=str(input('Ingrese el nuevo valor\n=>'))
                            sql="update datosPersonales set "+campoMod+"=%s where rutListado=%s"
                            try:    
                                self.cursor.execute(sql,(nuevoValor,rutListado))
                                self.conexion.commit()
                                print("Dato modificado exitosamente.")
                            except Exception as err:
                                self.conexion.rollback()
                                print("Error al modificar el dato: \n"+err)
                            break
                        elif modi=='n':
                            break
                        else:
                            print('(s/n)=>')

            elif tabla=='cargasFamiliares':
                system('cls')
                while datos is not None:
                    print('\
                            Rut de la Carga:\t',datos[0],'\n\
                            Nombre:\t',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguna de las cargas? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutCarga=input('Inserte el rut de la nueva Carga Familiar:\n=>')
                                nombreCarga=input('Inserte el nombre de la Carga Familiar:\n=>')
                                sexoCarga=input('inserte el sexo de la nueva Carga Familiar:\n=>')
                                parentescoCarga=input('inserte el parentesco con la Carga:\n=>')
                                sql1='insert into cargasFamiliares (rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga)\
                                    values (%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga))
                                    self.conexion.commit()
                                    print("Carga Familiar añadida exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir la carga: \n",err)
                                break
                            elif eleccion=="2":
                                rutCarga=input('Inserte el rut de la Carga Familiar que desea eliminar:')
                                sql2='delete from cargasFamiliares where rutCarga=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutCarga,))
                                    self.conexion.commit()
                                    print("Carga eliminada exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar la carga: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')
            elif tabla=='contactosEmergencia':
                system('cls')
                while datos is not None:
                    print('\
                            Rut del Contacto:\t',datos[0],'\n\
                            Nombre del Contacto:\t',datos[1],'\n\
                            Prioridad:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n\
                            Parentesco:\t',datos[4],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguno de los contactos? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutEmer=input('Inserte el rut del nuevo Contacto:\n=>')
                                nombreEmer=input('Inserte el nombre del Contacto:\n=>')
                                prioridadEmer=int(input('Inserte la Prioridad del contacto (de forma númerica):\n=>'))
                                telefonoEmer=input('Inserte el telefono del Contacto:\n=>')
                                relacionEmer=input('Inserte la relación que tiene con el contacto:\n=>')
                                sql1='insert into contactosEmergencia (rutEmer,rutListado,nombreEmer,numPrioridad,telefonoEmer,relacionEmer)\
                                    values (%s,%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutEmer,rutListado,nombreEmer,prioridadEmer,telefonoEmer,relacionEmer))
                                    self.conexion.commit()
                                    print("Contacto de Emergencia añadido exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir el contacto: \n",err)
                                break
                            elif eleccion=="2":
                                rutEmer=input('Inserte el rut del contacto de Emergencia que desea eliminar:\n=>')
                                sql2='delete from contactosEmergencia where rutEmer=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutEmer,))
                                    self.conexion.commit()
                                    print("Contacto eliminado exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar el Contacto: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')

        except Exception as err:
            self.conexion.rollback()
            print(err)

    def modificarCuentaUsuario(self):

        system('cls')
        print('Modificar Datos del Empleado:\n')
        
        rutListado = input('Ingrese el Rut del Empleado:\n=>')
        
        # Preguntar que tipo de dato modificaremos, para seleccionar la tabla adecuada.
        while True:
            system('cls')
            tabla=input(\
            '¿Que tabla desea modificar?:\n\
            Datos de Usuario\t(1)\n\
            Datos Laborales\t(2)\n\
            Datos Personales\t(3)\n\
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
        if tabla=="listadoTrabajadores":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar:\n\
                        Usuario\t(1)\n\
                        Contraseña\t(2)\n\
                        Perfil de la Cuenta\t(3)\n=>')
                if campo=="1":
                    campo="usuario"
                    break
                elif campo=="2":
                    campo="contraseña"
                    break
                elif campo=="3":
                    campo="perfilCuenta"
                    break

        elif tabla=="datosLaborales":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar\
                            Departamento\t(1)\n\
                            Área\t(2)\n\
                            Cargo\t(3)\n=>')
                if campo=="1":
                    campo="Departamento"
                    break
                elif campo=="2":
                    campo="Area"
                    break
                elif campo=="3":
                    campo="Cargo"
                    break
        elif tabla=="datosPersonales":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar\n\
                            Nombre\t(1)\n\
                            Sexo\t(2)\n\
                            Dirección\t(3)\n\
                            Telefono\t(4)\n=>')
                if campo=="1":
                    campo="NombrePer"
                    break
                elif campo=="2":
                    campo="sexoPer"
                    break
                elif campo=="3":
                    campo="direccionPer"
                    break
                elif campo=="4":
                    campo="telefonoPer"
                    break
        nuevoValor=input('Ingrese el nuevo valor para: '+campo+':\n=>')
        # se arma la consulta con los datos especificados anteriormente
        sql1="update "+tabla+" set "+campo+"=%s where rutListado=%s"

        try:
            self.cursor.execute(sql1, (nuevoValor, rutListado))
            self.conexion.commit()
            print("Datos del empleado modificados exitosamente.")
        except Exception as err:
            self.conexion.rollback()
            print("Error al modificar los datos del empleado: \n"+err)

    def eliminarCuentaUsuario(self):
        system('cls')
        rutListado = str(input('Ingrese el Rut del Empleado a eliminar:\n'))
        while True:
            confirm=input('¿Esta seguro de querer eliminar este rut? (s/n):').lower()
            if confirm=='s':
        # se realizan varias instrucciones para eliminar de todas las tablas, los datos
        # con los que coincida el rut del trabajador ingresado.
                sql1="delete from ListadoTrabajadores where RutListado = %s"
                sql2="delete from DatosLaborales where RutListado = %s"
                sql3="delete from ContactosEmergencia where RutListado = %s"
                sql4="delete from DatosPersonales where RutPer = %s"
                sql5="delete from CargasFamiliares where RutListado = %s"

                try:
                    self.cursor.execute(sql1,(rutListado,))
                    self.cursor.execute(sql2,(rutListado,))
                    self.cursor.execute(sql3,(rutListado,))
                    self.cursor.execute(sql4,(rutListado,))
                    self.cursor.execute(sql5,(rutListado,))
                    self.conexion.commit()
                    print("Empleado eliminado exitosamente de todas las tablas.")
                    break
                except Exception as err:
                    self.conexion.rollback()
                    print("Ha ocurrido un error al eliminar el empleado: ",err)
                    break
            elif confirm=='n':
                break
            else:
                system('cls')
                print('Error vuelva a ingresar la confirmación')

    def listadoTrabajadores(self):

    # Es una consulta en donde se juntan los datos de 2 tablas para mostrar todos los trabajadores.
    # posteriormente le consultaremos si filtrara la tabla
        sql1='select l.rutListado,p.NombrePer,p.SexoPer,p.DireccionPer,p.TelefonoPer,l.cargo\
              from datosPersonales p,datosLaborales l\
              where l.rutListado=p.rutPer'
        self.cursor.execute(sql1)
        empleado=self.cursor.fetchone()
        #ordenarlos de forma más legible
        while empleado is not None:
            print(' Rut',empleado[0],'\n\
                    Nombre:',empleado[1],'\n\
                    Cargo:',empleado[5],'\n\
                    Sexo:',empleado[2],'\n\
                    Dirección:',empleado[3],'\n\
                    Teléfono:',empleado[4],'\n\
                    ')
            empleado=self.cursor.fetchone()
        #idealmente la presentación deberia ser en filas y no en columnas, pero
        #debido al tiempo se mantendra de esta forma
            
        while True:
            filtro=input('¿Desea filtrar los resultados (s/n)?')
            if filtro=='s':
                while True:
                    system('cls')
                    filt=input('Ingrese el filtro que desea agregar:\n\
                                Sexo\t(1)\n\
                                Cargo\t(2)\n\
                                Área y Departamento\t(3)\n=>')
                    if filt=="1":
                        fil="sexoPer"
                        break
                    elif filt=="2":
                        fil="cargo"
                        break
                    elif filt=="3":
                        fil="area,departamento"
                        break
                if fil=='area,departamento':
                    #como son 2 condiciones en una, tiene que separarse para ejecutar la instrucción
                    #correctamente sin afectar a los otros casos.
                    condicion1=input('Escriba el Área:\n=>')
                    condicion2=input('Escriba el Departamento:\n=>')

                    sql2='select l.rutListado,p.NombrePer,p.SexoPer,p.DireccionPer,p.TelefonoPer,l.cargo\
                            from datosPersonales p,datosLaborales l\
                            where l.rutListado=p.rutPer and\
                            l.Area like "'+condicion1+'%" and l.Departamento like "'+condicion2+'%"'
                    self.cursor.execute(sql2)
                    empleado=self.cursor.fetchone()
                    print("Listado Filtrado:\n")
                    while empleado is not None:
                        print('\
                            Rut:', empleado[0],'\n\
                            Nombre:',empleado[1],'\n\
                            Cargo:',empleado[5],'\n\
                            Sexo:',empleado[2],'\n\
                            Dirección:',empleado[3],'\n\
                            Teléfono:',empleado[4],'\n\
                            ')
                        empleado=self.cursor.fetchone()
                else:
                    condicion=str(input('Escriba como comienza el dato a filtrar:\n=>'))
                    sql0='\
                    select l.rutListado,p.NombrePer,p.SexoPer,p.DireccionPer,p.TelefonoPer,l.cargo\
                    from datosPersonales p,datosLaborales l\
                    where l.rutListado=p.rutPer and\
                    '+fil+' like "'+condicion+'%"\
                    '
                    print('fil=',fil,'condicion=',condicion)
                    self.cursor.execute(sql0)
                    empleado=self.cursor.fetchone()
                    print("Listado Filtrado:\n")
                    while empleado is not None:
                        print('\
                            Rut: ',empleado[0],'\n\
                            Nombre: ',empleado[1],'\n\
                            Cargo: ',empleado[5],'\n\
                            Sexo: ',empleado[2],'\n\
                            Dirección: ',empleado[3],'\n\
                            Teléfono: ',empleado[4],'\n\
                            ')
                        empleado=self.cursor.fetchone()
            elif filtro=='n':
                break
            
            else:
                system('cls')
                print('Error de elección')
            break
        sleep(1)

###         Funciones de RRHH           ###
class DatabaseRRHH:
    def __init__(self,usuario,contraseña):

        self.usuario=usuario
        # Establecemos la conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host='localhost',         # Dirección del servidor Default:'192.168.1.7'
            user=str(usuario),        # Usuario de la base de datos
            database='nomina',        # Nombre de la base de datos
            password=str(contraseña)  # Contraseña de la base de datos
        )
        # Creamos un cursor para ejecutar queries
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    def ingresarEmpleado(self):
        #Es necesario que la BD cuente con 1 rut de Personal de RRHH para el ingreso de datos
        #Para facilitar el proceso se ha designado 1 Rut para Personal de RRHH
        RutPersonalRRHH='20200200-2'
        system('cls')
        print('Datos de Cuenta, Nuevo Empleado:\n')
        #Se Procede a rellenar los datos necesarios para completar el formulario.
        #Es necesario iniciar por la taba de ListadoTrabajadores, para rellenar el resto de datos.

        ###         Datos de Cuenta            ###
        rutListado=str(input('Ingrese el Rut del Nuevo Empleado:\n=>'))
        usuario=str(input('Ingrese el nombre de Usuario que tendra la cuenta del trabajador:\n=>'))
        contraseña=str(input('Ingrese la contraseña de la cuenta del trabajador:\n=>'))
        while True:
            system('cls')
            print("Rut:",rutListado,"\nUsuario:",usuario)
            perfil=int(input(\
                            'Tipos de Perfil:\
                            \nEmpleado:\t1\
                            \nPersonal_RRHH:\t2\
                            \n=>'))
            if perfil==1:
                perfilPersonal="empleado"
                break
            elif perfil==2:
                perfilPersonal="personal_rrhh"
                break
            else:
                system('cls')
                print('Opción Invalida')
        #con los datos ya preparados, se arma la instrucción
        sql1="insert into listadoTrabajadores (rutListado,rutPersonalRRHH,usuario,contraseña,perfilCuenta) values (%s, %s, %s, %s, %s)"
        try:
            #se ejecuta la instruccion, si esta llega correctamente se actualiza con el commit.
            self.cursor.execute(sql1, (rutListado,RutPersonalRRHH,usuario,contraseña,perfilPersonal))            
            self.conexion.commit()
        except Exception as err:
            #En caso de que ocurra un error, se realizara un rollback de emergencia y se informara el error ocurrido.
            self.conexion.rollback()
            print(err)

        ###         Datos Personales        ###

        system('cls')
        print('Datos Personales:\nRut:',rutListado,'\n')
        #rutPer corresponde al mismo trabajador del rutListado, la variable apunta al mismo dato.
        rutPer=rutListado
        nombrePer=str(input('Ingrese el nombre del Trabajador:\n=>'))
        while True:
            sexoPer=str(input('Ingrese su Sexo:\nH=Hombre\nM=Mujer\nO=Otro\n=>')).lower()
            if sexoPer=='h':
                sexoPer="Hombre"
                break
            elif sexoPer=='m':
                sexoPer="Mujer"
                break
            elif sexoPer=="o":
                sexoPer="Otro"
                break
            else:
                print("Error al ingresar su sexo")

        direccionPer=str(input('Ingrese la dirección del trabajador:\n=>'))
        telefonoPer=str(input('Ingrese el telefono del trabajador:\n=>'))

        sql2="insert into datosPersonales (rutPer,rutListado, nombrePer,sexoPer, direccionPer, telefonoPer) values (%s, %s, %s, %s, %s,%s)"
        try:
            self.cursor.execute(sql2, (rutPer,rutListado,nombrePer,sexoPer,direccionPer, telefonoPer))            
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Datos Laborales         ###

        system('cls')
        print('Datos Laborales:\n')
        iDTrabajador=int(input('Ingrese el ID (númerico) del trabajador:\n=>'))
        departamento=str(input('Ingrese el departamento al que pertenece:\n=>'))
        area=str(input('Ingrese el Área del trabajador:\n=>'))
        cargo=str(input('Ingrese el Cargo del trabajador:\n=>'))
        print('Fecha de Ingreso:\n=>')
        fecha = input('Ingrese la fecha de ingreso (dd/mm/aaaa):\n=>')
        fechaIngreso=datetime.datetime.strptime(fecha,"%d/%m/%Y")

        sql3="insert into DatosLaborales (IdTrabajador,rutListado, Departamento,Area, Cargo, FechaIngreso) values (%s, %s, %s, %s, %s,%s)"
        try:
            
            self.cursor.execute(sql3, (iDTrabajador, rutListado,departamento,area ,cargo, fechaIngreso))            
            self.conexion.commit()
            system('cls')
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Contacto de Emergencia       ###

        # se da libertad de ingresar varios contactos o ninguno, pero por ahora el programa
        # necesita que exista por lo menos 1 ingreso
        while True:
            opcion=str(input('¿Desea agregar un contacto de Emergencia? (s/n):\n=>')).lower()
            if opcion=='s':
                system('cls')
                print('Contacto De Emergencia:\n=>')

                rutEmer=str(input('Ingrese el rut del contacto de Emergencia:\n=>'))
                nombreEmer=str(input('Ingrese el nombre del Contacto de Emergencia:\n=>'))
                numPrioridad=int(input('Ingrese la prioridad del Contacto de Emergencia (de forma númerica):\n=>'))
                telefonoEmer=str(input('Ingrese el telefono para el Contacto de Emergencia:\n=>'))
                relacionEmer=str(input('Ingrese la relación con el Contacto de Emergencia:\n=>'))

                sql4="insert into contactosEmergencia (rutEmer, rutListado, NombreEmer,\
                        numPrioridad,TelefonoEmer, RelacionEmer) values (%s, %s, %s, %s, %s,%s)"
                
                try:
                    self.cursor.execute(sql4, (rutEmer, rutListado,nombreEmer,numPrioridad,telefonoEmer ,relacionEmer))            
                    self.conexion.commit()
                    print('Contacto Ingresado Exitosamente')
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                system('cls')
                break
        ###         Carga Familiar    ###
        
        # se da libertad de ingresar varias cargas o ninguna, pero por ahora el programa
        # necesita que exista por lo menos 1 ingreso
        while True:
            print('Carga Familiar:\n')
            opcion=str(input('¿Desea ingresar una carga familiar? (s/n)\n=>')).lower()
            if opcion=="s":
                rutCarga=str(input('Ingrese el Rut de la Carga Familiar:\n=>'))
                nombreCarga=str(input('Ingrese el nombre de la Carga Familiar:\n=>'))
                while True:
                    sexoCarga=str(input('Ingrese el sexo de su carga:\nH=Hombre\nM=Mujer\nO=Otro\n=>')).lower()
                    if sexoCarga=='h':
                        sexoCarga="Hombre"
                        break
                    elif sexoCarga=='m':
                        sexoCarga="Mujer"
                        break
                    elif sexoCarga=="o":
                        sexoCarga="Otro"
                        break
                    else:
                        print("Error al ingresar su sexo")

                parentescoCarga=str(input('Ingrese el parentesco de la Carga Familiar:\n=>'))

                sql5="insert into CargasFamiliares (rutCarga, rutListado, nombreCarga, sexoCarga, parentescoCarga) \
                        values (%s, %s, %s, %s, %s)"
                try:
                    self.cursor.execute(sql5,(rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga))
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                break

    def verCuenta(self):
        system('cls')

    # se realiza una consulta dependiendo de la tabla que el usuario quiera visualizar
    # posteriormente se le dara la opción de modificar los datos de la tabla elegida.
        while True:
            system('cls')
            tabla=input(\
            '¿Que datos desea observar?:\n\
            Datos Personales:\t\t(1)\n\
            Cargas Familiares:\t\t(2)\n\
            Contactos de Emergencia:\t(3)\n\
            =>\
            ')
            if tabla=="1":
                tabla="datosPersonales"
                break
            elif tabla=="2":
                tabla="cargasFamiliares"
                break
            elif tabla=="3":
                tabla="contactosEmergencia"
                break
        if tabla=="datosPersonales":
            sql1='select rutPer,nombrePer,sexoPer,direccionPer,telefonoPer,l.rutListado from\
                  datosPersonales d, listadoTrabajadores l \
                  where d.rutListado=l.rutListado \
                  and l.usuario="'+self.usuario+'"'
        #la consulta se especifica utilizando el nombre de usuario como referencia en la busqueda
        elif tabla=='cargasFamiliares':
            sql1='select rutCarga,nombreCarga,sexoCarga,parentescoCarga,l.rutListado from\
                cargasFamiliares c, listadoTrabajadores l \
                where c.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        elif tabla=='contactosEmergencia':
            sql1='select rutEmer,nombreEmer,numPrioridad,telefonoEmer,relacionEmer,l.rutListado from\
                contactosEmergencia e, listadoTrabajadores l \
                where e.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        try:
            self.cursor.execute(sql1)
            datos=self.cursor.fetchone()
            rutListado=datos[-1]
            if tabla=='datosPersonales':
                while datos is not None:
                    # system('cls')
                    print('\
                            Rut:\t',datos[0],'\n\
                            Nombre:',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Dirección:',datos[3],'\n\
                            Telefono:',datos[4],'\n')
                    datos=self.cursor.fetchone()
                    while True:
                        modi=input('¿Desea Modificar alguno de los datos? (s/n)\n=>').lower()
                        if modi=='s':
                            while True:
                                system('cls')
                                campoMod=input('Ingrese el campo que desea modificar:\n\
                                    Nombre\t(1)\n\
                                    Sexo:\t(2)\n\
                                    Direccion:\t(3)\n\
                                    Telefono\t(4)\n=>')
                                if campoMod=="1":
                                    campoMod="nombrePer"
                                    break
                                elif campoMod=="2":
                                    campoMod="sexoPer"
                                    break
                                elif campoMod=="3":
                                    campoMod="direccionPer"
                                    break
                                elif campoMod=="4":
                                    campoMod="telefonoPer"
                                    break
                            nuevoValor=str(input('Ingrese el nuevo valor\n=>'))
                            sql="update datosPersonales set "+campoMod+"=%s where rutListado=%s"
                            try:    
                                self.cursor.execute(sql,(nuevoValor,rutListado))
                                self.conexion.commit()
                                print("Dato modificado exitosamente.")
                            except Exception as err:
                                self.conexion.rollback()
                                print("Error al modificar el dato: \n"+err)
                            break
                        elif modi=='n':
                            break
                        else:
                            print('(s/n)=>')

            elif tabla=='cargasFamiliares':
                system('cls')
                while datos is not None:
                    print('\
                            Rut de la Carga:\t',datos[0],'\n\
                            Nombre:\t',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguna de las cargas? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutCarga=input('Inserte el rut de la nueva Carga Familiar:\n=>')
                                nombreCarga=input('Inserte el nombre de la Carga Familiar:\n=>')
                                sexoCarga=input('inserte el sexo de la nueva Carga Familiar:\n=>')
                                parentescoCarga=input('inserte el parentesco con la Carga:\n=>')
                                sql1='insert into cargasFamiliares (rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga)\
                                    values (%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga))
                                    self.conexion.commit()
                                    print("Carga Familiar añadida exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir la carga: \n",err)
                                break
                            elif eleccion=="2":
                                rutCarga=input('Inserte el rut de la Carga Familiar que desea eliminar:')
                                sql2='delete from cargasFamiliares where rutCarga=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutCarga,))
                                    self.conexion.commit()
                                    print("Carga eliminada exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar la carga: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')
            elif tabla=='contactosEmergencia':
                system('cls')
                while datos is not None:
                    print('\
                            Rut del Contacto:\t',datos[0],'\n\
                            Nombre del Contacto:\t',datos[1],'\n\
                            Prioridad:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n\
                            Parentesco:\t',datos[4],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguno de los contactos? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutEmer=input('Inserte el rut del nuevo Contacto:\n=>')
                                nombreEmer=input('Inserte el nombre del Contacto:\n=>')
                                prioridadEmer=int(input('Inserte la Prioridad del contacto (de forma númerica):\n=>'))
                                telefonoEmer=input('Inserte el telefono del Contacto:\n=>')
                                relacionEmer=input('Inserte la relación que tiene con el contacto:\n=>')
                                sql1='insert into contactosEmergencia (rutEmer,rutListado,nombreEmer,numPrioridad,telefonoEmer,relacionEmer)\
                                    values (%s,%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutEmer,rutListado,nombreEmer,prioridadEmer,telefonoEmer,relacionEmer))
                                    self.conexion.commit()
                                    print("Contacto de Emergencia añadido exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir el contacto: \n",err)
                                break
                            elif eleccion=="2":
                                rutEmer=input('Inserte el rut del contacto de Emergencia que desea eliminar:\n=>')
                                sql2='delete from contactosEmergencia where rutEmer=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutEmer,))
                                    self.conexion.commit()
                                    print("Contacto eliminado exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar el Contacto: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')

        except Exception as err:
            self.conexion.rollback()
            print(err)
        
    def modificarCuentaUsuario(self):
        system('cls')
        print('Modificar Datos del Empleado:\n')
        
        rutListado = input('Ingrese el Rut del Empleado:\n=>')
        
        # Preguntar que tipo de dato modificaremos, para seleccionar la tabla adecuada.
        while True:
            system('cls')
            tabla=input(\
            '¿Que tabla desea modificar?:\n\
            Datos de Usuario\t(1)\n\
            Datos Laborales\t(2)\n\
            Datos Personales\t(3)\n\
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
        if tabla=="listadoTrabajadores":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar:\n\
                        Usuario\t(1)\n\
                        Contraseña\t(2)\n\
                        Perfil de la Cuenta\t(3)\n=>')
                if campo=="1":
                    campo="usuario"
                    break
                elif campo=="2":
                    campo="contraseña"
                    break
                elif campo=="3":
                    campo="perfilCuenta"
                    break

        elif tabla=="datosLaborales":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar\
                            Departamento\t(1)\n\
                            Área\t(2)\n\
                            Cargo\t(3)\n=>')
                if campo=="1":
                    campo="Departamento"
                    break
                elif campo=="2":
                    campo="Area"
                    break
                elif campo=="3":
                    campo="Cargo"
                    break
        elif tabla=="datosPersonales":
            while True:
                system('cls')
                campo=input('Ingrese el campo que desea modificar\n\
                            Nombre\t(1)\n\
                            Sexo\t(2)\n\
                            Dirección\t(3)\n\
                            Telefono\t(4)\n=>')
                if campo=="1":
                    campo="NombrePer"
                    break
                elif campo=="2":
                    campo="sexoPer"
                    break
                elif campo=="3":
                    campo="direccionPer"
                    break
                elif campo=="4":
                    campo="telefonoPer"
                    break
        nuevoValor=input('Ingrese el nuevo valor para: '+campo+':\n=>')
        # se arma la consulta con los datos especificados anteriormente
        sql1="update "+tabla+" set "+campo+"=%s where rutListado=%s"

        try:
            self.cursor.execute(sql1, (nuevoValor, rutListado))
            self.conexion.commit()
            print("Datos del empleado modificados exitosamente.")
        except Exception as err:
            self.conexion.rollback()
            print("Error al modificar los datos del empleado: \n"+err)

    def eliminarCuentaUsuario(self):
        system('cls')
        rutListado = str(input('Ingrese el Rut del Empleado a eliminar:\n'))
        while True:
            confirm=input('¿Esta seguro de querer eliminar este rut? (s/n):').lower()
            if confirm=='s':
        # se realizan varias instrucciones para eliminar de todas las tablas, los datos
        # con los que coincida el rut del trabajador ingresado.
                sql1="delete from ListadoTrabajadores where RutListado = %s"
                sql2="delete from DatosLaborales where RutListado = %s"
                sql3="delete from ContactosEmergencia where RutListado = %s"
                sql4="delete from DatosPersonales where RutPer = %s"
                sql5="delete from CargasFamiliares where RutListado = %s"

                try:
                    self.cursor.execute(sql1,(rutListado,))
                    self.cursor.execute(sql2,(rutListado,))
                    self.cursor.execute(sql3,(rutListado,))
                    self.cursor.execute(sql4,(rutListado,))
                    self.cursor.execute(sql5,(rutListado,))
                    self.conexion.commit()
                    print("Empleado eliminado exitosamente de todas las tablas.")
                    break
                except Exception as err:
                    self.conexion.rollback()
                    print("Ha ocurrido un error al eliminar el empleado: ",err)
                    break
            elif confirm=='n':
                break
            else:
                system('cls')
                print('Error vuelva a ingresar la confirmación')


###         Funciones de Empleados          ###

class DatabaseEmpleado:

    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        # Establecemos la conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host='localhost',         # Dirección del servidor Default:'192.168.1.7'
            user=str(usuario),        # Usuario de la base de datos
            database='nomina',        # Nombre de la base de datos
            password=str(contraseña)  # Contraseña de la base de datos
        )
        # Creamos un cursor para ejecutar queries
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    def verCuenta(self):
        system('cls')
    # se realiza una consulta dependiendo de la tabla que el usuario quiera visualizar
    # posteriormente se le dara la opción de modificar los datos de la tabla elegida.
        while True:
            system('cls')
            tabla=input(\
            '¿Que datos desea observar?:\n\
            Datos Personales:\t\t(1)\n\
            Cargas Familiares:\t\t(2)\n\
            Contactos de Emergencia:\t(3)\n\
            =>\
            ')
            if tabla=="1":
                tabla="datosPersonales"
                break
            elif tabla=="2":
                tabla="cargasFamiliares"
                break
            elif tabla=="3":
                tabla="contactosEmergencia"
                break
        if tabla=="datosPersonales":
            sql1='select rutPer,nombrePer,sexoPer,direccionPer,telefonoPer,l.rutListado from\
                  datosPersonales d, listadoTrabajadores l \
                  where d.rutListado=l.rutListado \
                  and l.usuario="'+self.usuario+'"'
        #la consulta se especifica utilizando el nombre de usuario como referencia en la busqueda
        elif tabla=='cargasFamiliares':
            sql1='select rutCarga,nombreCarga,sexoCarga,parentescoCarga,l.rutListado from\
                cargasFamiliares c, listadoTrabajadores l \
                where c.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        elif tabla=='contactosEmergencia':
            sql1='select rutEmer,nombreEmer,numPrioridad,telefonoEmer,relacionEmer,l.rutListado from\
                contactosEmergencia e, listadoTrabajadores l \
                where e.rutListado=l.rutListado \
                and l.usuario="'+self.usuario+'"'
        try:
            self.cursor.execute(sql1)
            datos=self.cursor.fetchone()
            rutListado=datos[-1]
            if tabla=='datosPersonales':
                while datos is not None:
                    # system('cls')
                    print('\
                            Rut:\t',datos[0],'\n\
                            Nombre:',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Dirección:',datos[3],'\n\
                            Telefono:',datos[4],'\n')
                    datos=self.cursor.fetchone()
                    while True:
                        modi=input('¿Desea Modificar alguno de los datos? (s/n)\n=>').lower()
                        if modi=='s':
                            while True:
                                system('cls')
                                campoMod=input('Ingrese el campo que desea modificar:\n\
                                    Nombre\t(1)\n\
                                    Sexo:\t(2)\n\
                                    Direccion:\t(3)\n\
                                    Telefono\t(4)\n=>')
                                if campoMod=="1":
                                    campoMod="nombrePer"
                                    break
                                elif campoMod=="2":
                                    campoMod="sexoPer"
                                    break
                                elif campoMod=="3":
                                    campoMod="direccionPer"
                                    break
                                elif campoMod=="4":
                                    campoMod="telefonoPer"
                                    break
                            nuevoValor=str(input('Ingrese el nuevo valor\n=>'))
                            sql="update datosPersonales set "+campoMod+"=%s where rutListado=%s"
                            try:    
                                self.cursor.execute(sql,(nuevoValor,rutListado))
                                self.conexion.commit()
                                print("Dato modificado exitosamente.")
                            except Exception as err:
                                self.conexion.rollback()
                                print("Error al modificar el dato: \n"+err)
                            break
                        elif modi=='n':
                            break
                        else:
                            print('(s/n)=>')

            elif tabla=='cargasFamiliares':
                system('cls')
                while datos is not None:
                    print('\
                            Rut de la Carga:\t',datos[0],'\n\
                            Nombre:\t',datos[1],'\n\
                            Sexo:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguna de las cargas? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutCarga=input('Inserte el rut de la nueva Carga Familiar:\n=>')
                                nombreCarga=input('Inserte el nombre de la Carga Familiar:\n=>')
                                sexoCarga=input('inserte el sexo de la nueva Carga Familiar:\n=>')
                                parentescoCarga=input('inserte el parentesco con la Carga:\n=>')
                                sql1='insert into cargasFamiliares (rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga)\
                                    values (%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutCarga,rutListado,nombreCarga,sexoCarga,parentescoCarga))
                                    self.conexion.commit()
                                    print("Carga Familiar añadida exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir la carga: \n",err)
                                break
                            elif eleccion=="2":
                                rutCarga=input('Inserte el rut de la Carga Familiar que desea eliminar:')
                                sql2='delete from cargasFamiliares where rutCarga=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutCarga,))
                                    self.conexion.commit()
                                    print("Carga eliminada exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar la carga: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')
            elif tabla=='contactosEmergencia':
                system('cls')
                while datos is not None:
                    print('\
                            Rut del Contacto:\t',datos[0],'\n\
                            Nombre del Contacto:\t',datos[1],'\n\
                            Prioridad:\t',datos[2],'\n\
                            Parentesco:\t',datos[3],'\n\
                            Parentesco:\t',datos[4],'\n')
                    datos=self.cursor.fetchone()
                while True:
                    modi=input('¿Desea Agregar o Eliminar alguno de los contactos? (s/n)\n=>').lower()
                    if modi=='s':
                        while True:
                            eleccion=input('Ingrese la acción que desea realizar:\n\
                                Agregar:\t(1)\n\
                                Eliminar:\t(2)\n\
                                n=>')
                            if eleccion=="1":
                                rutEmer=input('Inserte el rut del nuevo Contacto:\n=>')
                                nombreEmer=input('Inserte el nombre del Contacto:\n=>')
                                prioridadEmer=int(input('Inserte la Prioridad del contacto (de forma númerica):\n=>'))
                                telefonoEmer=input('Inserte el telefono del Contacto:\n=>')
                                relacionEmer=input('Inserte la relación que tiene con el contacto:\n=>')
                                sql1='insert into contactosEmergencia (rutEmer,rutListado,nombreEmer,numPrioridad,telefonoEmer,relacionEmer)\
                                    values (%s,%s,%s,%s,%s,%s)'
                                try:    
                                    self.cursor.execute(sql1,(rutEmer,rutListado,nombreEmer,prioridadEmer,telefonoEmer,relacionEmer))
                                    self.conexion.commit()
                                    print("Contacto de Emergencia añadido exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al añadir el contacto: \n",err)
                                break
                            elif eleccion=="2":
                                rutEmer=input('Inserte el rut del contacto de Emergencia que desea eliminar:\n=>')
                                sql2='delete from contactosEmergencia where rutEmer=%s'
                                try:    
                                    self.cursor.execute(sql2,(rutEmer,))
                                    self.conexion.commit()
                                    print("Contacto eliminado exitosamente.")
                                except Exception as err:
                                    self.conexion.rollback()
                                    print("Error al eliminar el Contacto: \n",err)
                                break
                            else:
                                system('cls')
                                print('Error en la opción')
                            modi='n'
                    elif modi=='n':
                        break
                    else:
                        print('(s/n)=>')

        except Exception as err:
            self.conexion.rollback()
            print(err)