import sympy as sp


class RLCCircuit:
    def __init__(self, R, L, C):
        self.R = R          # Ohms
        self.L = L / 1000   # mH → H
        self.C = C / 1e6    # µF → F

    def transfer_function(self):
        s = sp.symbols('s')
        H = 1 / (self.L * self.C * s**2 + self.R * self.C * s + 1)
        return sp.simplify(H)
