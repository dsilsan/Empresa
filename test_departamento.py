from unittest import TestCase
from Departamento import *
from Empleado import *
from mockito import *
__author__ = 'David'


class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        res = Departamento("Informatica", 1)
        # Generate a mock from a class
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        # Mock method calls
        when(emp1).get_salario().thenReturn(4000)
        when(emp2).get_salario().thenReturn(4000)
        when(emp3).get_salario().thenReturn(4000)
        res.intro_empleado(emp1)
        res.intro_empleado(emp2)
        res.intro_empleado(emp3)
        print(res.get_salario_total())
        self.assertNotEqual(res, 12000)

    def test_get_salario_total_mensual(self):
        res = Departamento("Informatica", 1)
        # Generate a mock from a class
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        # Mock method calls
        when(emp1).get_salario().thenReturn(4000)
        when(emp2).get_salario().thenReturn(4000)
        when(emp3).get_salario().thenReturn(4000)
        res.intro_empleado(emp1)
        res.intro_empleado(emp2)
        res.intro_empleado(emp3)
        print(res.get_salario_total())
        print(res.get_salario_total_mensual())
        self.assertNotEqual(res, 1000)