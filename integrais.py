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

    area_riemann = soma_de_riemann(f, a, b, n)
    area_exata = integral_exata(f, a, b)
    erro = abs(area_exata - area_riemann)

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(x_curva, y_curva, color="navy", linewidth=2,
            label=f"f(x) = {expressao}")

    ax.fill_between(x_curva, y_curva, color="skyblue", alpha=0.5,
                    label="Area exata = integral de f(x)")

    ax.bar(x_ret, f(x_ret), width=largura, align="edge",
           color="orange", edgecolor="black", alpha=0.4,
           label=f"{n} retangulos (Soma de Riemann)")

    ax.axvline(a, color="green", linestyle="--", linewidth=1)
    ax.axvline(b, color="green", linestyle="--", linewidth=1)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

