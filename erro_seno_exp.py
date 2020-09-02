# vitor alves pavani
# 01/09/2020
# Python 3.8.2 on win32


import math
from exponencial import exponencial
from seno import seno


"""
f(x,y,..)
erro_f = |df/dx * erro_x| + |df/dy * erro_y| ...
"""


def erro_xy(x, erro_x, y, erro_y):
    "propagação de erro para f(x,y) = x*y"
    return (abs(x*erro_y) + abs(y*erro_x))


def main():
    x = float(input("digite um valor para x: "))
    sen_x = seno(x)
    exp_x = exponencial(x)
    err_sen = abs(sen_x - math.sin(x))
    err_exp = abs(exponencial(x) - math.exp(x))
    real_sen_exp = math.sin(x) * math.exp(x)
    aprx_sen_exp = sen_x * exp_x
    print(sen_x * err_exp)
    print(exp_x * err_sen)

    err_aprx = erro_xy(sen_x, err_sen, exp_x, err_exp)
    err_real = abs(real_sen_exp - aprx_sen_exp)

    print(f"math.sin(x) * math.exp(x): {real_sen_exp:.15f}")
    print(f"seno(x) * exponencial(x): {aprx_sen_exp:.15f}")
    print(f"Erro propagado: {err_aprx:.15f}")
    print(f"Erro real: {err_real:.15f}")
    print(f"Diferença entre erros: {abs(err_real - err_aprx):.15f}")

if __name__ == "__main__":
    main()
