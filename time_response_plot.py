import numpy as np
from scipy import signal

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class TimeResponseCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(figsize=(6, 3))
        super().__init__(self.fig)

        self.ax = self.fig.add_subplot(111)
        self.fig.tight_layout()

    def plot_step_response(self, R, L_mH, C_uF):
        self.ax.clear()

        # Unit conversion
        L = L_mH / 1000      # mH → H
        C = C_uF / 1e6      # µF → F

        # Transfer function
        num = [1]
        den = [L * C, R * C, 1]

        system = signal.TransferFunction(num, den)

        # Step response
        t, y = signal.step(system)

        self.ax.plot(t, y)
        self.ax.set_title("Step Response")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Amplitude")
        self.ax.grid(True)

        self.draw()
