#!/usr/bin/python
# -*- coding: utf-8 -*-


class Cuadrante:
    """docstring for ClassName"""
    def __init__(self, valor=None, nivel=None,
                 nw=None, ne=None, se=None, sw=None):
        self.valor = valor
        self.nivel = nivel
        self.poblacion = None
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.resultado = None

    @classmethod
    def crear_cuadrante(cls, valor=None, nivel=None,
                        nw=None, ne=None, se=None, sw=None):
        # Comprobar que no existe otro igual
        if nivel == 0:
            # print("> soy un cuadrante de nivel 0")
            return cls(valor, 0)
        else:
            print("> soy un cuadrante de nivel ", nivel)
            return cls(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

    def generacion(self):
        if self.resultado is not None:
            print("resultado ya calculado antes")
            return self.resultado
        else:
            print("calcular el resultado")

    def expandir(self):
        pass
