__author__ = 'David'


class Empleado():
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        self.nom = nombre
        self.ape = apellidos
        self.dni = dni
        self.dir = direccion
        self.eda = edad
        self.email = email
        self.sal = salario

    def get_salario(self):
        return self.sal

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nom + " " + self.ape


emp1 = Empleado("david","silva","49028333s","c/falsa",24,"a@a.com",2000)
emp2 = Empleado("antonio","silva","49028332s","c/falsa",26,"a@a.com",2500)
emp3 = Empleado("pedro","silva","49028331s","c/falsa",28,"a@a.com",3000)
