import numpy as np
from scipy import signal

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class BodePlotCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(figsize=(6, 4))
        super().__init__(self.fig)

        self.ax_mag = self.fig.add_subplot(211)
        self.ax_phase = self.fig.add_subplot(212)

        self.fig.tight_layout()

    def plot(self, R, L_mH, C_uF):
        # Clear old plots
        self.ax_mag.clear()
        self.ax_phase.clear()

        # Unit conversion
        L = L_mH / 1000      # mH → H
        C = C_uF / 1e6      # µF → F

        # Transfer function
        num = [1]
        den = [L * C, R * C, 1]

        system = signal.TransferFunction(num, den)

        w, mag, phase = signal.bode(system)

        # Magnitude plot
        self.ax_mag.semilogx(w, mag)
        self.ax_mag.set_ylabel("Magnitude (dB)")
        self.ax_mag.set_title("Bode Magnitude")
        self.ax_mag.grid(True)

        # Phase plot
        self.ax_phase.semilogx(w, phase)
        self.ax_phase.set_ylabel("Phase (deg)")
        self.ax_phase.set_xlabel("Frequency (rad/s)")
        self.ax_phase.set_title("Bode Phase")
        self.ax_phase.grid(True)

        self.draw()
