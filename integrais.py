import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def soma_de_riemann(f, a, b, n):
    largura = (b - a) / n
    x_ret = np.linspace(a, b - largura, n)
    area = np.sum(largura * f(x_ret))
    return area

def integral_exata(f, a, b):
    resultado, _ = quad(f, a, b)
    return resultado

def gerar_grafico(f, a, b, n, expressao="f(x)"):
    x_curva = np.linspace(a, b, 300)
    y_curva = f(x_curva)

    largura = (b - a) / n
    x_ret = np.linspace(a, b - largura, n)

    area_riemann = soma_de_riemann(f, a, b, n)
    area_exata = integral_exata(f, a, b)
    erro = abs(area_exata - area_riemann)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(x_curva, y_curva, color="navy", linewidth=2,
             label=f"f(x) = {expressao}")
    ax1.fill_between(x_curva, y_curva, color="skyblue", alpha=0.6,
                     label="Area exata = integral de f(x)")
    ax1.axvline(a, color="green", linestyle="--", linewidth=1)
    ax1.axvline(b, color="green", linestyle="--", linewidth=1)
    ax1.axhline(0, color="black", linewidth=0.8)
    ax1.set_title("Area exata (integral)", fontsize=13)
    ax1.set_xlabel("eixo x")
    ax1.set_ylabel("eixo y")
    ax1.text(0.05, 0.95, f"Area exata: {area_exata:.6f}",
             transform=ax1.transAxes, fontsize=11, verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
    ax1.legend(loc="lower right")
    ax1.grid(True, linestyle=":", alpha=0.6)

    ax2.plot(x_curva, y_curva, color="navy", linewidth=2,
             label=f"f(x) = {expressao}")
    ax2.bar(x_ret, f(x_ret), width=largura, align="edge",
            color="orange", edgecolor="black", alpha=0.5,
            label=f"{n} retangulos (Soma de Riemann)")
    ax2.axvline(a, color="green", linestyle="--", linewidth=1)
    ax2.axvline(b, color="green", linestyle="--", linewidth=1)
    ax2.axhline(0, color="black", linewidth=0.8)
    ax2.set_title(f"Aproximacao por Soma de Riemann  -  n = {n}", fontsize=13)
    ax2.set_xlabel("eixo x")
    ax2.set_ylabel("eixo y")
    texto = (f"n (retangulos): {n}\n"
             f"Area aproximada: {area_riemann:.6f}\n"
             f"Erro: {erro:.6f}")
    ax2.text(0.05, 0.95, texto, transform=ax2.transAxes,
             fontsize=11, verticalalignment="top",
             bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))
    ax2.legend(loc="lower right")
    ax2.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()
    plt.show()

    return area_riemann, area_exata, erro