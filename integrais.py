import numpy as np
import matplotlib.pyplot as plt

def soma_de_riemann(f, a, b, n):
    largura = (b - a) / n
    x_ret = np.linspace(a, b - largura, n)
    area = np.sum(largura * f(x_ret))
    return area

def integral_exata(f, a, b):
    n = 100000
    largura = (b - a) / n
    x = np.linspace(a, b - largura, n)
    return np.sum(largura * f(x))

def gerar_grafico(f, a, b, n, expressao="f(x)"):
    x_curva = np.linspace(a, b, 300)
    y_curva = f(x_curva)

    largura = (b - a) / n
    x_ret = np.linspace(a, b - largura, n)