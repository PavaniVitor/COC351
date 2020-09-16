# vitor alves pavani
# 15/09/2020
# Python 3.6.9 on Linux

# https://nm.mathforcollege.com/chapter-03-04-newton-raphson-method/

from exponencial import exponencial


def f_aux_ln(n, x=None):
    """Função auxiliar a qual utilizaremos para procurar a raiz"""
    if x:
        f_aux_ln.x = x
    return (exponencial(n) - f_aux_ln.x)


def df_aux_ln(n):
    """Função auxiliar a qual utilizaremos para procurar a raiz"""
    return exponencial(n)


def nr_root(f_x, df_x, x, n=50, d=1e-8):
    """Método Newton-Raphson para encontrar raizes

    Parametros: 
    f_x(function): função em que será feita a busca pela raiz
    df_X(function): derivada da de função derivada de f_x
    x(float): valor inicial da busca 
    n(int): número de interações 
    d(float): criterio de parada, retorna se abs(aprox_raiz) < d
    --------------------------------
    return (aprox_raiz , erro)


    """
    x_p = 0
    for i in range(n):

        x = x - f_x(x)/df_x(x)

        if i > 0 and abs(x) < d:
            break

        if i != n-1:
            x_p = x

    erro = abs((x - x_p)/x) * 100

    return (x, erro)


def ln_nr(x, s):
    """Calcula ln(x) utilizando o método Newton-Raphson

    Parametros:
    x(float): ln(x)
    s(int): número de iterações
    --------------------------------
    return (aprox_raiz , erro)
    """
    if x == 1:
        return (0, 0)
    f_aux_ln(1, x)  # inicializa os valores da função auxiliar
    p = 0.7  # ponto inicial de busca

    return nr_root(f_aux_ln, df_aux_ln, p, n=s, d=1e-8)
