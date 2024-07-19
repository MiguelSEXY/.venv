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
            host='localhost',         # Dirección del servidor / WinServer:'192.168.1.7'
            user=self.usuario,              # Usuario de la base de datos
            database='nomina',        # Nombre de la base de datos
            password=contraseña       # Contraseña de la base de datos
        )
        # Creamos un cursor para ejecutar queries
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()
    
    def ingresarEmpleado(self):
        #Es necesario que la BD cuente con 1 rut de Personal de RRHH para el ingreso de datos
        #Para facilitar el proceso se ha designado 1 Rut para Personal de RRHH
        RutPersonalRRHH=   '20200200-2'
        system('cls')
        print('Datos de Cuenta, Nuevo Empleado:\n')
        #Se Procede a rellenar los datos necesarios para completar el formulario.
        #Es necesario iniciar por la taba de ListadoTrabajadores, para rellenar el resto de datos.
        #Por ahora se rellanaran los datos de forma secuencial más que de forma lógica.
        rutListado=str(input('Ingrese el Rut del Nuevo Empleado:\n'))
        usuario=str(input('Ingrese el nombre de Usuario que tendra la cuenta del trabajador:\n'))
        contraseña=str(input('Ingrese la contraseña de la cuenta del trabajador:\n'))
        while True:
            system('cls')
            print("Rut:",rutListado,"\nUsuario:",usuario)
            perfil=int(input(\
                            'Tipos de Perfil:\
                            \nEmpleado:\t1\
                            \nPersonal_RRHH:\t2\
                            '))
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
        sql1="insert into listadoTrabajadores (rutListado,rutPersonalRRHH,usuario, contraseña,perfilCuenta) values (%s, %s, %s, %s, %s)"
        try:
            #se ejecuta la instruccion, si esta llega correctamente se actualiza con el commit.
            self.cursor.execute(sql1, (rutListado,RutPersonalRRHH,usuario ,contraseña,perfilPersonal))            
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
        nombrePer=str(input('Ingrese el nombre del Trabajador:\n'))
        sexoPer=str(input('Ingrese su Sexo:\n\
                           H=Hombre\tM=Mujer\tO=Otro\n')).lower()
        while sexoPer!="Hombre" and sexoPer!="Mujer" and sexoPer!="Otro":
            sexoPer=str(input('Ingrese su Sexo:\n\
                               H=Hombre\tM=Mujer\tO=Otro\n')).lower()
            if sexoPer=='h':
                sexoPer="Hombre"
            elif sexoPer=='m':
                sexoPer="Mujer"
            elif sexoPer=="o":
                sexoPer="Otro"
            else:
                print("Error al ingresar su sexo")

        direccionPer=str(input('Ingrese la dirección del trabajador:\n'))
        telefonoPer=str(input('Ingrese el domicilio del trabajador:\n'))

        sql2="insert into DatosLaborales (rutPer,rutListado, nombrePer,sexoPer, direccionPer, telefonoPer) values (%s, %s, %s, %s, %s,%s)"
        try:
            self.cursor.execute(sql2, (rutPer, rutListado,nombrePer,sexoPer ,direccionPer, telefonoPer))            
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Datos Laborales         ###

        system('cls')
        print('Datos Laborales:\n')
        iDTrabajador=int(input('Ingrese el ID (númerico) del trabajador:\n'))
        departamento=str(input('Ingrese el departamento al que pertenece:\n'))
        area=str(input('Ingrese el Área del trabajador:\n'))
        cargo=str(input('Ingrese el Cargo del trabajador:\n'))
        print('Fecha de Ingreso:\n')
        fecha = input('Ingrese la fecha de ingreso (dd/mm/aaaa):\n')
        fechaIngreso=datetime.datetime.strptime(fecha,"%d/%m/%Y")

        sql3 = "insert into DatosLaborales (IdTrabajador,rutListado, Departamento,Area, Cargo, FechaIngreso) values (%s, %s, %s, %s, %s,%s)"
        try:
            
            self.cursor.execute(sql3, (iDTrabajador, rutListado,departamento,area ,cargo, fechaIngreso))            
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Contacto de Emergencia       ###
        while True:
            system('cls')
            opcion=str(input('¿Desea agregar un contacto de Emergencia? (s/n):\n')).lower()
            if opcion=='s':
                system('cls')
                print('Contacto De Emergencia:\n')

                numPrioridad=int(input('Ingrese la prioridad del Contacto de Emergencia (1 al 5):\n'))
                nombreEmer=  str(input('Ingrese el nombre del Contacto de Emergencia:\n'))
                telefonoEmer=str(input('Ingrese el Telefono para el Contacto de Emergencia:\n'))
                relacionEmer=str(input('Ingrese la relación con el Contacto de Emergencia:\n'))

                sql4 = "insert into contactosEmergencia (NumPrioridad, rutListado, NombreEmer,\
                        TelefonoEmer, RelacionEmer) values (%s, %s, %s, %s, %s)"
                
                try:
                    self.cursor.execute(sql4, (numPrioridad, rutListado,nombreEmer,telefonoEmer ,relacionEmer))            
                    self.conexion.commit()
                    system('cls')
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                break
        ###         Carga Familiar    ###

        while True:
            system('cls')
            print('Carga Familiar:\n')
            opcion=str(input('¿Desea ingresar una carga familiar? (s/n)')).lower()
            if opcion=="s":
                rutCarga=str(input('Ingrese el Rut de la Carga Familiar:\n'))
                nombreCarga=str(input('Ingrese el nombre de la Carga Familiar:\n'))
                sexoCarga=str(input('Ingrese el Sexo de la Carga Familiar:\
                                    \nH=Hombre\nM=Mujer\nO=Otro\n')).lower()
                while sexoCarga!="Hombre" and sexoCarga!="Mujer" and sexoCarga!="Otro":
                    sexoCarga=str(input('Ingrese el Sexo de la Carga Familiar:\
                                        \nH=Hombre\nM=Mujer\nO=Otro\n')).lower()
                    if sexoCarga=='h':
                        sexoCarga="Hombre"
                    elif sexoCarga=='m':
                        sexoCarga="Mujer"
                    elif sexoCarga=="o":
                        sexoCarga="Otro"
                    else:
                        print("Error en el ingreso del sexo de la persona")

                parentescoCarga=str(input('Ingrese el parentesco de la Carga Familiar:\n'))

                sql5 = "insert into CargasFamiliares (rutCarga, rutListado, nombreCarga, sexoCarga, parentescoCarga) \
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
        #FALTA ORDENAR
    # Es una consulta en donde se juntan los datos de varias tablas
    # y la condicion que limita el resultado es el nombre del usuario que esta conectado.
        sql1='\
        select l.rutListado,l.Usuario,l.PerfilCuenta,\
        p.NombrePer,p.SexoPer,p.DireccionPer,p.TelefonoPer,c.nombreCarga,c.ParentescoCarga,    e.NombreEmer,e.relacionEmer,e.numPrioridad \
        from listadoTrabajadores l,datosPersonales p,cargasFamiliares c,ContactosEmergencia e\
        where l.rutListado=p.rutPer\
        and l.rutListado=c.rutListado\
        and l.rutListado=e.rutListado\
        and l.usuario="'+str(self.usuario)+'"'
        
        try:
            self.cursor.execute(sql1)
            datos=self.cursor.fetchone()
            #esta parte falta modificar para ser presentados de forma adecuada
            print(datos)
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
                campo=input('Ingrese el campo que desea modificar\
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
        sql1="update"+repr(tabla)+"set"+repr(campo)+"=%s where rutListado=%s"
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
        system('cls')
        confirma=input('¿Esta seguro de que desea eliminar el usuario con rut:',rutListado,'? (s/n):\n')
        while confirma!='s' or confirma!='n':
            system('cls')
            confirma=input('¿Esta seguro de que desea eliminar el usuario con rut:',rutListado,'? (s/n):\n')
        if confirma=='s':
            # se realizan varias instrucciones para eliminar de todas las tablas, los datos
            # con los que coincida el rut del trabajador ingresado.
            sql1="delete from ListadoTrabajadores where RutListado = %s"
            sql2="delete from DatosLaborales where RutListado = %s"
            sql3="delete from ContactosEmergencia where RutListado = %s"
            sql4="delete from DatosPersonales where RutPer = %s"
            sql5="delete from CargasFamiliares where RutListado = %s"

            try:
                self.cursor.execute(sql1,(rutListado))
                self.cursor.execute(sql2,(rutListado))
                self.cursor.execute(sql3,(rutListado))
                self.cursor.execute(sql4,(rutListado))
                self.cursor.execute(sql5,(rutListado))
                self.conexion.commit()
                print("Empleado eliminado exitosamente de todas las tablas.")
            except Exception as err:
                self.conexion.rollback()
                print("Ha ocurrido un error al eliminar el empleado: "+err)
        else:
            print('Se ha cancelado la operación')
            sleep(1)
            system('cls')

    def listadoTrabajadores(self):

    # Es una consulta en donde se juntan los datos de varias tablas de todos los trabajadores.
    #la \ permite ordenar de mejor forma la instrucción
        sql1=\
        'select l.rutListado,l.Usuario,l.PerfilCuenta,\
        p.NombrePer,p.SexoPer,p.TelefonoPer,\
        d.IdTrabajador,d.Departamento,d.Area,d.Cargo,d.FechaIngreso\
        from listadoTrabajadores l,datosPersonales p,datosLaborales d\
        where l.rutListado=p.rutPer\
        and l.rutListado=d.rutListado'
        
        try:
            self.cursor.execute(sql1)
            datos=self.cursor.fetchall()
            print(datos)
        except Exception as err:
            self.conexion.rollback()
            print(err)

###         Funciones de RRHH           ###
class DatabaseRRHH:
    def __init__(self,usuario,contraseña):


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
        #Para facilitar el proceso se han designado 1 Rut para Jefe y Personal de RRHH
        RutJefe=           '10100100-1'
        RutPersonalRRHH=   '20200200-2'
        system('cls')
        print('Datos de Cuenta, Nuevo Empleado:\n')
        #Se Procede a rellenar los datos necesarios para completar el formulario.
        #Es necesario iniciar por la taba de ListadoTrabajadores, para rellenar el resto de datos.
        #Por ahora se rellanaran los datos de forma secuencial más que de forma lógica.
        rutListado=str(input('Ingrese el Rut del Nuevo Empleado:\n'))
        usuario=str(input('Ingrese el nombre de Usuario que tendra la cuenta del trabajador:\n'))
        contraseña=str(input('Ingrese la contraseña de la cuenta del trabajador:\n'))
        while True:
            perfil=int(input('''Tipos de Perfil:\n\nEmpleado:      \t1\nPersonal_RRHH:\t2
                            '''))
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
        sql1="insert into ListadoTrabajadores values ("+repr(rutListado)+","+repr(RutPersonalRRHH)+","+repr(usuario)+","+repr(contraseña)+","+repr(perfilPersonal)+")"
        try:
            #se ejecuta la instruccion, si esta llega correctamente se actualiza con el commit.
            self.cursor.execute(sql1)
            self.conexion.commit()
        except Exception as err:
            #En caso de que ocurra un error, se realizara un rollback de emergencia y se informara el error ocurrido.
            self.conexion.rollback()
            print(err)

        ###         Datos Personales        ###
        system('cls')
        print('Datos Personales:\n')
        rutPer=rutListado
        nombrePer=str(input('Ingrese el nombre del Trabajador:\n'))
        sexoPer=str(input('Ingrese el Sexo del Trabajador:\nH=Hombre\nM=Mujer\nO=Otro (lo que tu sientas que eres)\n'))
        direccionPer=str(input('Ingrese la dirección del trabajador:\n'))
        telefonoPer=str(input('Ingrese el domicilio del trabajador:\n'))

        sql2="insert into DatosPersonales values ("+repr(rutPer)+","+repr(rutListado)+","+repr(nombrePer)+","+repr(sexoPer)+","+repr(direccionPer)+","+repr(telefonoPer)+")"
        try:
            self.cursor.execute(sql2)
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

        ###         Datos Laborales         ###
        #Error Aun Sin Comprender 2055 Lost Conexion
        # system('cls')
        # self.cursor.reset()
        # print('Datos Laborales:\n')
        # iDTrabajador=int(input('Ingrese el ID (númerico) del trabajador:\n'))
        # departamento=str(input('Ingrese el departamento al que pertenece:\n'))
        # area=str(input('Ingrese el Sexo del trabajador:\n'))
        # cargo=str(input('Ingrese el Cargo del trabajador:\n'))
        # print('Fecha de Ingreso:\n')
        # fechaIngreso=datetime.now().strftime('%Y/%m/%d')
        # print(fechaIngreso)
        
        # sql3="insert into datoslaborales values (",(iDTrabajador),","+repr(rutListado)+","+repr(departamento)+","+repr(area)+","+repr(cargo)+","+repr(fechaIngreso)+"))"
  
        # try:
        #     self.cursor.execute(sql3)
        #     self.conexion.commit()
        # except Exception as err:
        #     self.conexion.rollback()
        #     print(err)

        ###         Cargas Familiares       ###
        while True:
            system('cls')
            print('Carga Familiar:\n')
            opcion=str(input('¿Posee más cargas familiares? (s/n)'))
            if opcion=="s":
                rutCarga=str(input('Ingrese el Rut de la Carga Familiar:\n'))
                nombreCarga=str(input('Ingrese el nombre de la Carga Familiar:\n'))
                sexoCarga=str(input('Ingrese el Sexo de la Carga Familiar:\nH=Hombre\nM=Mujer\nO=Otro\n'))
                parentescoCarga=str(input('Ingrese el parentesco de la Carga Familiar:\n'))

                sql4="insert into CargasFamiliares values ("+repr(rutCarga)+","+repr(rutListado)+","+repr(nombreCarga)+","+repr(sexoCarga)+","+repr(parentescoCarga)+")"

                try:
                    self.cursor.execute(sql4)
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                break

        ###         Contactos Emergencia    ###
        system('cls')
        print('Contacto De Emergencia:\n')
        numPrioridad=int(input('Ingrese la prioridad del Contacto de Emergencia (1 al 5):\n'))
        nombreEmer=str(input('Ingrese el nombre del Contacto de Emergencia:\n'))
        telefonoEmer=str(input('Ingrese el Telefono para el Contacto de Emergencia:\n'))
        relacionEmer=str(input('Ingrese la relación con el Contacto de Emergencia:\n'))

        sql5="insert into ContactosEmergencia values (",(numPrioridad),","+repr(rutListado)+","+repr(nombreEmer)+","+repr(telefonoEmer)+","+repr(relacionEmer)+")"

        try:
            self.cursor.execute(sql5)
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

    def verCuenta(self):
        pass
        
    def modificarCuentaUsuario(self):
        pass

    def eliminarCuentaUsuario(self):
        pass


###         Funciones de Empleados          ###
class DatabaseEmpleado:
    def __init__(self,usuario,contraseña):

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
        pass