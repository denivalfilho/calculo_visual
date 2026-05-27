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

    ax.set_title(f"Calculo de Area por Integral  -  n = {n}", fontsize=14)
    ax.set_xlabel("eixo x")
    ax.set_ylabel("eixo y")

    texto = (f"n (retangulos): {n}\n"
             f"Area aproximada: {area_riemann:.6f}\n"
             f"Area exata (integral): {area_exata:.6f}\n"
             f"Erro: {erro:.6f}")
    ax.text(0.05, 0.95, texto, transform=ax.transAxes,
            fontsize=11, verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

    ax.legend(loc="lower right")
    ax.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.show()

    return area_riemann, area_exata, erro