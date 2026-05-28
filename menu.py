import numpy as np
import integrais

def criar_funcao(expressao):
    def f(x):
        return eval(expressao, {"x": x, "np": np,
                                "sin": np.sin, "cos": np.cos,
                                "tan": np.tan, "exp": np.exp,
                                "log": np.log, "sqrt": np.sqrt,
                                "pi": np.pi, "e": np.e})
    return f