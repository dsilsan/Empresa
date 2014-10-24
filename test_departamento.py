from unittest import TestCase
from Departamento import *
from Empleado import *

__author__ = 'David'



class TestDepartamento(TestCase):


    def test_get_salario_total(self):

        res=Departamento("Informatica",1)
        res.intro_empleado(emp1)
        res.intro_empleado(emp2)
        res.intro_empleado(emp3)
        print(res.get_salario_total())
        self.assertNotEqual(res,7500)
