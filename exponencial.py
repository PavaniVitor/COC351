# vitor alves pavani
# 01/09/2020
# Python 3.8.2 on win32
from math import exp

def fatorial(n):
    f = 1 
    if n==0:
      return f
    for i in range(1,n+1):
      f*=i
    return f
    
def exponencial(x, ordem=9):
    """
    retorna e^x aproximado até o termo n.
    """
    resultado = 0.0
    for i in range(ordem+1):
        resultado += x**i/fatorial(i)
    return resultado


if __name__ == "__main__":
    #x = 0.5
    x = float(input("Digite um valor para calcular e^x: "))
    print(f"Aproximação de ordem 9 para e^x: {exponencial(x):.15f}")
    print(f"Valor Computado por math.exp(x): {exp(x):.15f}")
    print(f"Erro: {abs(exp(x) - exponencial(x)):.15f}")
