__author__ = 'David'


class Departamento():
    def __init__(self, nombre_depto, id_depto):
        self.nomDpt = nombre_depto
        self.idDpt = id_depto
        self.lEmpleados = []

    def intro_empleado(self, Emp):
        self.lEmpleados.append(Emp)

    def get_nombre_dpto(self):
        return self.nomDpt

    def get_salario_total_mensual(self):
        total = 0
        for emp in self.lEmpleados:
            total += emp.get_salario()
        return total/12

    def get_salario_total(self):
        total = 0
        for emp in self.lEmpleados:
            total += emp.get_salario()
        return total
