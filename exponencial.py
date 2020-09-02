# vitor alves pavani
# 01/09/2020
# Python 3.8.2 on win32

import math


def exponencial(x, ordem=9):
    """
    retorna e^x aproximado até a ordem n.
    """
    if x <= 0 or x >= 1:
        print("X fora dos limites da função. (0 < x < 1)")
        return
    ordem += 1
    resultado = 0
    for i in range(ordem):
        resultado += x**i/math.factorial(i)
    return resultado


if __name__ == "__main__":
    #x = 0.5
    x = float(input("Digite um valor para calcular e^x: "))
    print(f"Aproximação de ordem 9 para e^x: {exponencial(x):.15f}")
    print(f"Valor Computado por math.exp(x): {math.exp(x):.15f}")
    print(f"Erro: {abs(math.exp(x) - exponencial(x)):.15f}")
