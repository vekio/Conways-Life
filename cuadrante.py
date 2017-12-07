#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


class Cuadrante:
    """Clase Cuadrante para el juego Conway's life."""
    def __init__(self, valor=None, nivel=None, poblacion=None,
                 nw=None, ne=None, se=None, sw=None):
        self.valor = valor
        self.nivel = nivel
        self.poblacion = poblacion
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.resultado = None

    @classmethod
    def crear_cuadrante(cls, valor=None, nivel=None, poblacion=0,
                        nw=None, ne=None, se=None, sw=None):
        """Crea Cuadrante cuadrantes unicos"""
        # Comprobar que no existe otro igual
        if nivel == 0:
            if valor == "X":
                poblacion = 1
            # print("> soy un cuadrante de nivel 0 poblacion ", poblacion)
            return cls(valor, 0, poblacion)
        else:
            for x in nw, ne, sw, se:
                poblacion = x.poblacion + poblacion
            if nivel == 3:
                print(poblacion)
            # print("> soy un cuadrante de nivel ", nivel,"poblacion ", poblacion)
            return cls(nivel=nivel, poblacion=poblacion, nw=nw, ne=ne, sw=sw, se=se)

    def generacion(self):
        """Crea la siguiente generacion de celulas vivas/muertas."""
        # Se devuelve el resultado de este cuadrante si ya ha sido generado
        if self.resultado is not None:
            print("resultado ya calculado antes")
            return self.resultado
        # Sino se realiza el cálculo, se almacena en resultado y se devuelve
        else:
            # Antes comprobamos si hace falta expandir
            self.expandir()
            print("calcular el resultado")
            return self.resultado

    def expandir(self):
        """Comprueba si la poblacion de celulas vivas se encuentra
        en el subcuadrante central del nivel superior."""
        pass
