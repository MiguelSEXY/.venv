listaEmpleados=["Empleado_Roberto"]
listaRRHH=["RRHH_Miguel"]
listaJefes=["JEFES_Moises","root"]

#Se mantendran en 3 listas los empleados ya registrados
#Medida temporal antes de preparar un fetch para sacar los datos de una BD

class Usuario():
    def __init__(self,cuentaUsuario):

        self.cuenta=cuentaUsuario
#dependiendo de a que lista corresponda el usuario se le da una categoria distinta.
        if self.cuenta in listaEmpleados:
            self.categoria="empleado"
        elif self.cuenta in listaRRHH:
            self.categoria="rrhh"
        elif self.cuenta in listaJefes:
            self.categoria="jefe"
        else:
            self.categoria="Invasor"
