
# vitor alves pavani
# 15/09/2020
# Python 3.6.9 on Linux

# https://nm.mathforcollege.com/chapter-03.03-bisection-method/

from exponencial import exponencial


def bis_root(f_x, x_l, x_u, n=50, d=0):
    """Método da bisecção para encontrar raizes

    Parametros: 
    f_x(function): função em que será feita a busca pela raiz
    x_l(float): inicio do intervalo de busca de raizes
    x_u(float): fim do intervalo de busca de raizes
    n(int): número de interações 
    d(float): criterio de parada, retorna se abs(xl - x_u) < d
    --------------------------------
    return (aprox_raiz , erro)
    """

    x_p = 0
    for i in range(n):

        x_m = (x_l + x_u)/2

        if f_x(x_l)*f_x(x_m) == 0:
            return (x_m, 0)
        elif f_x(x_l)*f_x(x_m) < 0:
            x_l = x_l
            x_u = x_m
        elif f_x(x_l)*f_x(x_m) > 0:
            x_l = x_m
            x_u = x_u


        if i > 0 and abs(x_u - x_l) < d:
            break

        if i != n-1:
            x_p = x_m

    erro = abs((x_m - x_p)/x_m) * 100

    return (x_m, erro)


def f_aux_ln(n, x=None):
    """Função auxiliar a qual utilizaremos para procurar a raiz"""
    if x:
        f_aux_ln.x = x
    return (exponencial(n) - f_aux_ln.x)


def ln_bis(x, s):
    """Calcula ln(x) utilizando o método bisecção

    Parametros:
    x(float): ln(x)
    s(int): número de iterações
    --------------------------------
    return (aprox_raiz , erro)
    """
    if x == 1:
        return (0, 0)
    f_aux_ln(1, x)  # inicializa os valores da função auxiliar
    a = 0
    b = 0.7

    return bis_root(f_aux_ln, a, b, n=s, d=1e-8)
