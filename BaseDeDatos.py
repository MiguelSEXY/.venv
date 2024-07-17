import mysql.connector
from os import system
import datetime
from datetime import datetime
#se llama al modulo mysql.connector instalado previamente usando pip para descargar las dependencias 
###         Funciones de Jefe           ###
class DatabaseJEFE:
    # al instanciar 
    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        # Establecemos la conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host='localhost',         # Dirección del servidor / WinServer:'192.168.1.7'
            user=(usuario),           # Usuario de la base de datos
            database='nomina',        # Nombre de la base de datos
            password=(contraseña)     # Contraseña de la base de datos
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

        system('cls')
        print('Datos Laborales:\n')
        iDTrabajador=int(input('Ingrese el ID (númerico) del trabajador:\n'))
        departamento=str(input('Ingrese el departamento al que pertenece:\n'))
        area=str(input('Ingrese el Área del trabajador:\n'))
        cargo=str(input('Ingrese el Cargo del trabajador:\n'))
        print('Fecha de Ingreso:\n')
        fechaIngreso = input('Ingrese la fecha de ingreso (AAAA-MM-DD):\n')
        #Forma alternativa de armar la instruccion SQL
        sql3 = "INSERT INTO DatosLaborales (IdTrabajador,rutListado, Departamento,Area, Cargo, FechaIngreso) VALUES (%s, %s, %s, %s, %s,%s)"
  
        try:
            self.cursor.execute(sql3, (iDTrabajador, rutListado,departamento,area ,cargo, fechaIngreso))            
            self.conexion.commit()
        except Exception as err:
            self.conexion.rollback()
            print(err)

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

        sql5 = "INSERT INTO contactosEmergencia (NumPrioridad, rutListado, NombreEmer, TelefonoEmer, RelacionEmer) VALUES (%s, %s, %s, %s, %s)"
        
        try:
            self.cursor.execute(sql5, (numPrioridad, rutListado,nombreEmer,telefonoEmer ,relacionEmer))            
            self.conexion.commit()
            system('cls')
        except Exception as err:
            self.conexion.rollback()
            print(err)
        

    def verCuenta(self):
        #FALTA ORDENAR

    #Es una consulta en donde se juntan las tablas, ListadoTrabajadores,DatosPersonales,Contactos de Emergencia y cargas familiares, y la condicion que limita el resultado es el del usuario ya conectado.
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
            print(datos)
        except Exception as err:
            self.conexion.rollback()
            print(err)

    def modificarCuentaUsuario(self):
        pass

    def eliminarCuentaUsuario(self):
        system('cls')
        print('Rut del Empleado a Eliminar:\n')
        
        rutListado = input('Ingrese el Rut del Empleado a eliminar:\n')
        
        # Preparar las consultas SQL para eliminar al empleado de todas las tablas
        sql1 = "DELETE FROM ListadoTrabajadores WHERE RutListado = %s"
        sql2 = "DELETE FROM DatosLaborales WHERE RutListado = %s"
        sql3 = "DELETE FROM ContactosEmergencia WHERE RutListado = %s"
        sql4 = "DELETE FROM DatosPersonales WHERE RutPer = %s"
        sql5 = "DELETE FROM CargasFamiliares WHERE RutListado = %s"

        try:
            self.cursor.execute(sql1, (rutListado,))
            self.cursor.execute(sql2, (rutListado,))
            self.cursor.execute(sql3, (rutListado,))
            self.cursor.execute(sql4, (rutListado,))
            self.cursor.execute(sql5, (rutListado,))
            self.conexion.commit()
            print("Empleado eliminado exitosamente de todas las tablas.")
        except Exception as err:
            self.conexion.rollback()
            print("Error al eliminar al empleado: "+err)


    def listadoTrabajadores(self):
        #FALTA ORDENAR
         #Es una consulta en donde se juntan las tablas, ListadoTrabajadores,DatosPersonales,Contactos de Emergencia y cargas familiares, mostrando una tupla de todas los usuarios que cumplan con todas las partes de la consulta .
        sql1='\
        select l.rutListado,l.Usuario,l.PerfilCuenta,\
        p.NombrePer,p.SexoPer,p.DireccionPer,p.TelefonoPer,c.nombreCarga,c.ParentescoCarga,    e.NombreEmer,e.relacionEmer,e.numPrioridad \
        from listadoTrabajadores l,datosPersonales p,cargasFamiliares c,ContactosEmergencia e\
        where l.rutListado=p.rutPer\
        and l.rutListado=c.rutListado\
        and l.rutListado=e.rutListado'
        
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
        # area=str(input('Ingrese el Área del trabajador:\n'))
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