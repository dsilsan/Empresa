__author__ = 'David'


class Empresa():
    def __init__(self, nombre_empresa, cif, razon_social):
        self.nom = nombre_empresa
        self.cif = cif
        self.rs = razon_social
        self.lDepartamentos = []