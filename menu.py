import numpy as np
import integrais


def criar_funcao(expressao):
    def f(x):
        try:
            return eval(expressao, {"x": x, "np": np,
                                    "sin": np.sin, "cos": np.cos,
                                    "tan": np.tan, "exp": np.exp,
                                    "log": np.log, "sqrt": np.sqrt,
                                    "pi": np.pi, "e": np.e})
        except Exception as e:
            print(f"\n  Erro ao avaliar a funcao: {e}")
            return np.zeros_like(x)
    return f


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  Valor invalido. Digite um numero.")


def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("  Digite um numero inteiro maior que zero.")
        except ValueError:
            print("  Valor invalido. Digite um numero inteiro.")


def main():
    print("=" * 50)
    print("  VISUALIZADOR DE AREAS POR INTEGRAIS")
    print("=" * 50)
    print("Exemplos de funcao: x**2 + 1 | sin(x) | exp(x) | x**3")
    print()

    expressao = input("Digite a funcao f(x): ").strip()
    f = criar_funcao(expressao)

    try:
        f(1.0)
    except Exception as e:
        print(f"  Aviso: a expressao parece incorreta ({e}).")
        print("  O programa pode gerar um grafico zerado. Considere reiniciar.")

    a = ler_numero("Digite o limite inferior a: ")
    b = ler_numero("Digite o limite superior b: ")

    if a == b:
        print("\n  Nota: o limite inferior e igual ao superior. A area sera 0.")
    elif a > b:
        a, b = b, a
        print(f"  (limites trocados: a = {a}, b = {b})")

    print()
    print("Agora vamos gerar os graficos variando o n.")
    print("Aumente o n e veja a aproximacao melhorar!")
    print()

    while True:
        n = ler_inteiro_positivo("Digite o valor de n (retangulos): ")

        resultado = integrais.gerar_grafico(f, a, b, n, expressao)
        area_riemann, area_exata, erro = resultado

        print()
        print("-" * 50)
        print(f"  n = {n}")
        print(f"  Area aproximada (Riemann): {area_riemann:.6f}")
        print(f"  Area exata (integral):     {area_exata:.6f}")
        print(f"  Erro:                      {erro:.6f}")
        print("-" * 50)
        print()

        resposta = input("Gerar outro grafico com novo n? (s/n): ").strip().lower()
        print()
        if resposta != "s":
            print("Encerrando. Ate a proxima!")
            break


if __name__ == "__main__":
    main()
