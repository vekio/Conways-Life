#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan

from tabla_dispersion import TablaDispCer


class Cuadrante:
    """Clase Cuadrante para el juego Conway's life."""
    tabla_dispersion = TablaDispCer(m=1)

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
    def crear_cuadrante(cls, nivel=None, poblacion=0,
                        nw=None, ne=None, se=None, sw=None):
        """Crea Cuadrante cuadrantes unicos"""
        # Comprobar que no existe otro igual
        if nivel == 0:
            # print("> soy un cuadrante de nivel ", nivel,"poblacion ", poblacion)
            return cls(0, poblacion)
        else:
            clave = Cuadrante.hash_cuad(nw, ne, sw, se)
            cuad = Cuadrante.tabla_dispersion.buscar(clave)
            if cuad is None:
                for x in nw, ne, sw, se:
                    poblacion = x.poblacion + poblacion
                # if nivel == 3:
                #    print(poblacion)
                # print("> soy un cuadrante de nivel ", nivel,"poblacion ", poblacion)
                Cuadrante.tabla_dispersion.insertar(clave, cls(nivel, poblacion, nw=nw, ne=ne, sw=sw, se=se))
                return cls(nivel, poblacion, nw=nw, ne=ne, sw=sw, se=se)
            else:
                return cuad

    @classmethod
    def hash_cuad(cls, nw, ne, sw, se):
        h = hash(nw) + 11 * hash(ne) + 101 * hash(sw) + 1007 * hash(se)
        return int(h)

    def generacion2(self):
        """Crea la siguiente generacion de celulas vivas/muertas para un nivel 2."""
        vivas_nw = self.nw.poblacion + self.ne.nw.poblacion + self.ne.sw.poblacion + self.sw.nw.poblacion + self.sw.ne.poblacion + self.se.nw.poblacion
        vivas_ne = self.ne.poblacion + self.nw.ne.poblacion + self.nw.se.poblacion + self.sw.ne.poblacion + self.se.nw.poblacion + self.se.ne.poblacion
        vivas_sw = self.sw.poblacion + self.nw.sw.poblacion + self.nw.se.poblacion + self.ne.sw.poblacion + self.se.nw.poblacion + self.se.sw.poblacion
        vivas_se = self.se.poblacion + self.nw.se.poblacion + self.ne.sw.poblacion + self.ne.se.poblacion + self.sw.ne.poblacion + self.sw.se.poblacion
        # print(vivas_nw)
        # print(vivas_ne)
        # print(vivas_sw)
        # print(vivas_se)

        if self.nw.se.poblacion == 1:
            vivas_nw -= 1
            if vivas_nw == 2 or vivas_nw == 3:
                nw = Cuadrante.crear_cuadrante(0, 1)
            else:
                nw = Cuadrante.crear_cuadrante(0, 0)
        else:
            if vivas_nw == 3:
                nw = Cuadrante.crear_cuadrante(0, 1)
            else:
                nw = Cuadrante.crear_cuadrante(0, 0)

        if self.ne.sw.poblacion == 1:
            vivas_ne -= 1
            if vivas_ne == 2 or vivas_ne == 3:
                ne = Cuadrante.crear_cuadrante(0, 1)
            else:
                ne = Cuadrante.crear_cuadrante(0, 0)
        else:
            if vivas_ne == 3:
                ne = Cuadrante.crear_cuadrante(0, 1)
            else:
                ne = Cuadrante.crear_cuadrante(0, 0)

        if self.sw.ne.poblacion == 1:
            vivas_sw -= 1
            if vivas_sw == 2 or vivas_sw == 3:
                sw = Cuadrante.crear_cuadrante(0, 1)
            else:
                sw = Cuadrante.crear_cuadrante(0, 0)
        else:
            if vivas_sw == 3:
                sw = Cuadrante.crear_cuadrante(0, 1)
            else:
                sw = Cuadrante.crear_cuadrante(0, 0)

        if self.se.nw.poblacion == 1:
            vivas_se -= 1
            if vivas_se == 2 or vivas_se == 3:
                se = Cuadrante.crear_cuadrante(0, 1)
            else:
                se = Cuadrante.crear_cuadrante(0, 0)
        else:
            if vivas_se == 3:
                se = Cuadrante.crear_cuadrante(0, 1)
            else:
                se = Cuadrante.crear_cuadrante(0, 0)

        # print("--salgo generacion2--")
        return Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=nw, ne=ne, sw=sw, se=se)

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
                """
                n00 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.nw.nw.se, ne=self.nw.ne.sw, sw=self.nw.sw.ne, se=self.nw.se.nw)
                n01 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.nw.ne.se, ne=self.ne.nw.sw, sw=self.nw.se.ne, se=self.ne.sw.nw)
                n02 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.ne.nw.se, ne=self.ne.ne.sw, sw=self.ne.sw.ne, se=self.ne.se.nw)

                n10 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.nw.sw.se, ne=self.nw.se.sw, sw=self.sw.nw.ne, se=self.sw.ne.nw)
                n11 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.nw.se.se, ne=self.ne.sw.sw, sw=self.sw.ne.ne, se=self.se.nw.nw)
                n12 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.ne.sw.se, ne=self.ne.se.sw, sw=self.se.nw.ne, se=self.se.ne.nw)

                n20 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.sw.nw.se, ne=self.sw.ne.sw, sw=self.sw.sw.ne, se=self.sw.se.nw)
                n21 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.sw.ne.se, ne=self.se.nw.sw, sw=self.sw.se.ne, se=self.se.sw.nw)
                n22 = Cuadrante.crear_cuadrante(nivel=self.nivel - 2, nw=self.se.nw.se, ne=self.se.ne.sw, sw=self.se.sw.ne, se=self.se.se.nw)
                """
                n00 = self.nw.generacion()
                n01 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=self.nw.ne, ne=self.ne.nw, sw=self.nw.se, se=self.ne.sw).generacion()
                n02 = self.ne.generacion()

                n10 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=self.nw.sw, ne=self.nw.se, sw=self.sw.nw, se=self.sw.ne).generacion()
                n11 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=self.nw.se, ne=self.ne.sw, sw=self.sw.ne, se=self.se.nw).generacion()
                n12 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=self.ne.sw, ne=self.ne.se, sw=self.se.nw, se=self.se.ne).generacion()

                n20 = self.sw.generacion()
                n21 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=self.sw.ne, ne=self.se.nw, sw=self.sw.se, se=self.se.sw).generacion()
                n22 = self.se.generacion()


                m00 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=n00, ne=n01, sw=n10, se=n11)
                m01 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=n01, ne=n02, sw=n11, se=n12)
                m10 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=n10, ne=n11, sw=n20, se=n21)
                m11 = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=n11, ne=n12, sw=n21, se=n22)

                r00 = m00.generacion()
                r01 = m01.generacion()
                r10 = m10.generacion()
                r11 = m11.generacion()

                self.resultado = Cuadrante.crear_cuadrante(nivel=self.nivel - 1, nw=r00, ne=r01, sw=r10, se=r11)

                # print("--salgo generacion--")
                return self.resultado

    def expandir(self):
        """Comprueba si la poblacion de celulas vivas se encuentra
        en el subcuadrante central del nivel superior."""
        # Cogemos la poblacion del cuadrante y sumamos la del sub sub cuadrante
        # si coinciden no hace falta expandir
        sub_po = self.nw.se.se.poblacion + self.ne.sw.sw.poblacion + self.sw.ne.ne.poblacion + self.se.nw.nw.poblacion
        # print("poblacion subsub ", sub_po, "pobacion total", self.poblacion)
        if sub_po == self.poblacion:
            return self
        # Hace falta expandir
        nw = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=Cuadrante.crear_vacio(self.nivel - 1), sw=Cuadrante.crear_vacio(self.nivel - 1), se=self.nw)
        ne = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=Cuadrante.crear_vacio(self.nivel - 1), sw=self.ne, se=Cuadrante.crear_vacio(self.nivel - 1))
        sw = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=Cuadrante.crear_vacio(self.nivel - 1), ne=self.sw, sw=Cuadrante.crear_vacio(self.nivel - 1), se=Cuadrante.crear_vacio(self.nivel - 1))
        se = Cuadrante.crear_cuadrante(nivel=self.nivel, nw=self.se, ne=Cuadrante.crear_vacio(self.nivel - 1), sw=Cuadrante.crear_vacio(self.nivel - 1), se=Cuadrante.crear_vacio(self.nivel - 1))
        expandido = Cuadrante.crear_cuadrante(nivel=self.nivel + 1, nw=nw, ne=ne, sw=sw, se=se)
        expandido = expandido.expandir()
        # print("--salgo expandir--")
        return expandido

    @classmethod
    def crear_vacio(cls, nivel):
        """Crea un arbol vacio del nivel especificado"""
        if nivel == 1:
            nw = Cuadrante.crear_cuadrante(nivel - 1, 0)
            ne = Cuadrante.crear_cuadrante(nivel - 1, 0)
            sw = Cuadrante.crear_cuadrante(nivel - 1, 0)
            se = Cuadrante.crear_cuadrante(nivel - 1, 0)
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)
        else:
            nw = Cuadrante.crear_vacio(nivel - 1)
            ne = Cuadrante.crear_vacio(nivel - 1)
            sw = Cuadrante.crear_vacio(nivel - 1)
            se = Cuadrante.crear_vacio(nivel - 1)
            return Cuadrante.crear_cuadrante(nivel=nivel, nw=nw, ne=ne, sw=sw, se=se)

        def generacion2(self):
            """Aplica directamente las reglas de vida"""
            pass
