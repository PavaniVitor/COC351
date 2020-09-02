# vitor alves pavani
# 01/09/2020
# Python 3.8.2 on win32

import math


def seno(x, ordem=9):
    """
    retorna sen(x) aproximado até a ordem n.
    """
    if x <= 0 or x >= 1:
        print("X fora dos limites da função. (0 < x < 1)")
        return

    resultado = 0
    for i in range(int(((ordem-1)/2)+1)):
        sinal = (-1)**i
        resultado += sinal*x**(1+2*i)/math.factorial(1+2*i)

    return resultado


if __name__ == "__main__":
    x = math.pi/4
    #x = float(input("Digite um valor para calcular e^x: "))
    print(f"Aproximação de ordem 9 para sen(x): {seno(x):.15f}")
    print(f"Valor Computado por math.sin(x): {math.sin(x):.15f}")
    print(f"Erro: {abs(math.sin(x) - seno(x)):.15f}")
