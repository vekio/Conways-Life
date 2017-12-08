#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


class Cuadrante:
    """Clase Cuadrante para el juego Conway's life."""
    def __init__(self, nivel=None, poblacion=None,
                 nw=None, ne=None, se=None, sw=None):
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
            return cls(0, poblacion)
        else:
            for x in nw, ne, sw, se:
                poblacion = x.poblacion + poblacion
            if nivel == 3:
                print(poblacion)
            # print("> soy un cuadrante de nivel ", nivel,"poblacion ", poblacion)
            return cls(nivel=nivel, poblacion=poblacion, nw=nw, ne=ne, sw=sw, se=se)

    def get_pixel(self, x, y):
        pass

    def generacion2(self):
        """Crea la siguiente generacion de celulas vivas/muertas para un nivel 2."""
        vivas_nw = self.nw.poblacion + self.ne.nw.poblacion + self.ne.sw.poblacion + self.sw.nw.poblacion + self.sw.ne.poblacion + self.se.nw.poblacion
        vivas_ne = self.ne.poblacion + self.nw.ne.poblacion + self.nw.se.poblacion + self.sw.ne.poblacion + self.se.nw.poblacion + self.se.ne.poblacion
        vivas_sw = self.sw.poblacion + self.nw.sw.poblacion + self.nw.se.poblacion + self.ne.sw.poblacion + self.se.nw.poblacion + self.se.sw.poblacion
        vivas_se = self.se.poblacion + self.nw.se.poblacion + self.ne.sw.poblacion + self.ne.se.poblacion + self.sw.ne.poblacion + self.sw.se.poblacion

        if self.nw.se.poblacion == 1:
            vivas_nw -= 1
        if vivas_nw == 2 or vivas_nw == 3:
            nw = Cuadrante.crear_cuadrante(nivel=0, poblacion=1)
        else:
            nw = Cuadrante.crear_cuadrante(nivel=0, poblacion=0)

        if self.ne.sw.poblacion == 1:
            vivas_ne -= 1
        if vivas_ne == 2 or vivas_ne == 3:
            ne = Cuadrante.crear_cuadrante(nivel=0, poblacion=1)
        else:
            ne = Cuadrante.crear_cuadrante(nivel=0, poblacion=0)

        if self.sw.ne.poblacion == 1:
            vivas_sw -= 1
        if vivas_sw == 2 or vivas_sw == 3:
            sw = Cuadrante.crear_cuadrante(nivel=0, poblacion=1)
        else:
            sw = Cuadrante.crear_cuadrante(nivel=0, poblacion=0)

        if self.se.nw.poblacion == 1:
            vivas_se -= 1
        if vivas_se == 2 or vivas_se == 3:
            se = Cuadrante.crear_cuadrante(nivel=0, poblacion=1)
        else:
            se = Cuadrante.crear_cuadrante(nivel=0, poblacion=0)

        return Cuadrante.crear_cuadrante(nw=nw, ne=ne, sw=sw, se=se)

    def generacion(self):
        """Crea la siguiente generacion de celulas vivas/muertas."""
        # Se devuelve el resultado de este cuadrante si ya ha sido generado
        if self.resultado is not None:
            return self.resultado
        # Sino se realiza el cálculo, se almacena en resultado y se devuelve
        else:
            # Los niveles 0 y 1 no se realizan calculos
            # Generacion de nivel 2
            if self.nivel == 2:
                self.resultado = self.generacion2()
                return self.resultado
            else:
                # generacion de 4 subcudrantes de un nivel menos
                self.resultado = self.generacion()
                return self.resultado

    def expandir(self):
        """Comprueba si la poblacion de celulas vivas se encuentra
        en el subcuadrante central del nivel superior."""
        expandir = False
        while expandir:
            if self.nw.nw.poblacion != 0 or self.nw.ne.poblacion != 0 or self.nw.sw.poblacion != 0:
                expandir = True
            elif self.ne.nw.poblacion != 0 or self.ne.ne.poblacion != 0 or self.ne.se.poblacion != 0:
                expandir = True
            elif self.sw.nw.poblacion != 0 or self.sw.sw.poblacion != 0 or self.ne.se.poblacion != 0:
                expandir = True
            elif self.se.ne.poblacion != 0 or self.se.sw.poblacion != 0 or self.se.se.poblacion != 0:
                expandir = True
            # No hace falta expandir, devolvemos el mismo
            return self
        # Hace falta expandir
        nw = Cuadrante.crear_cuadrante(nive=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=Cuadrante.crear_vacio(self.nivel - 1), sw=Cuadrante.crear_vacio(self.nivel - 1), se=self.nw)
        ne = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=Cuadrante.crear_vacio(self.nivel - 1), sw=self.ne, se=Cuadrante.crear_vacio(self.nivel - 1))
        sw = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=self.sw, sw=Cuadrante.crear_vacio(self.nivel - 1), se=Cuadrante.crear_vacio(self.nivel - 1))
        se = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=self.se, ne=Cuadrante.crear_vacio(self.nivel - 1), sw=Cuadrante.crear_vacio(self.nivel - 1), se=Cuadrante.crear_vacio(self.nivel - 1))
        expandido = Cuadrante.crear_cuadrante(nivel=self.nivel + 1, nw=nw, ne=ne, sw=sw, se=se)
        return expandido

        @classmethod
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
