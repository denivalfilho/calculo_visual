# Visualizador de Áreas por Integrais

Aplicação didática que mostra visualmente o conceito de área sob uma curva usando a **Soma de Riemann** e a biblioteca **Matplotlib**.

## Como usar

```bash
pip install numpy matplotlib scipy
python menu.py
```

Digite a função, os limites do intervalo e o número de retângulos. Aumente o `n` e veja a aproximação melhorar.

## Exemplos de função

```
x**2 + 1
sin(x)
exp(x)
x**3 - 2*x
```

## Arquivos

| Arquivo | Descrição |
|---|---|
| `integrais.py` | Cálculo da Soma de Riemann e geração do gráfico |
| `menu.py` | Interface no terminal |
