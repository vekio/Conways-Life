#!/usr/bin/python
# -*- coding: utf-8 -*-

# Alberto Castañeiras - albcast
# Jorge Chana - jorchan


class pp(object):
    """docstring for pp"""
    tabla = []

    def __init__(self, nivel):
        self.nivel = nivel

    @classmethod
    def crear_pp(cls, nivel):
        pp.tabla.append(nivel)
        return cls(nivel)


if __name__ == '__main__':
    print(pp.tabla)
    x = pp.crear_pp(2)
    print(x.tabla)
    print(pp.tabla)
    y = pp.crear_pp(5)
    print(y.tabla)
    print(pp.tabla)
    print(x.tabla)
