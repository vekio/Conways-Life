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
            # Los niveles 0 y 1 no se realizan calculos
            if self.nivel == 0 or self.nivel == 1:
                pass
            elif self.nivel == 2:
                self.generacion2()
            else:
                # Antes comprobamos si hace falta expandir
                self.expandir()
                print("calcular el resultado")
                return self.resultado

    def expandir(self):
        """Comprueba si la poblacion de celulas vivas se encuentra
        en el subcuadrante central del nivel superior."""
        expandir = False
        while expandir:
            if self.nw.nw.poblacion != 0 or self.nw.ne.poblacion != 0 or self.nw.sw.poblacion != 0:
                expandir = True
            elif self.ne.nw.poblacion != 0 or self.ne.ne.poblacion != 0 or self.ne.sw.poblacion != 0:
                expandir = True
            elif self.sw.nw.poblacion != 0 or self.sw.sw.poblacion != 0 or self.ne.se.poblacion != 0:
                expandir = True
            elif self.se.ne.poblacion != 0 or self.se.sw.poblacion != 0 or self.se.se.poblacion != 0:
                expandir = True
            # No hace falta expandir, devolvemos -1
            return -1
        # Hace falta expandir
        ### crear uno vacio de un nivel superior
        ### añadir en las posiciones centrales el que invoca el metodo
        expandido = self.crear_vacio(self.nivel + 1)
        pass

        def crear_vacio(self, nivel):
            """Crea un arbol vacio del nivel especificado"""
            valor = "."
            if nivel == 1:
                nw = self.crear_cuadrante(valor, nivel - 1)
                ne = self.crear_cuadrante(valor, nivel - 1)
                sw = self.crear_cuadrante(valor, nivel - 1)
                se = self.crear_cuadrante(valor, nivel - 1)
                return self.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)
            else:
                nw = self.crear_vacio(nivel - 1)
                ne = self.crear_vacio(nivel - 1)
                sw = self.crear_vacio(nivel - 1)
                se = self.crear_vacio(nivel - 1)
                return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

        def generacion2(self):
            """Aplica directamente las reglas de vida"""
            pass
