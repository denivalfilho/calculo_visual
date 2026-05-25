import numpy as np
import matplotlib.pyplot as plt

def soma_de_riemann(f, a, b, n):
    largura = (b - a) / n
    x_ret = np.linspace(a, b - largura, n)
    area = np.sum(largura * f(x_ret))
    return area