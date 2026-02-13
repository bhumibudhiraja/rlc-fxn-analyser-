import sys
from PyQt6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene,
    QPushButton, QVBoxLayout, QWidget, QLabel
)
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtCore import Qt

from resistor import ResistorItem
from capacitor import CapacitorItem
from inductor import InductorItem
from circuit_model import RLCCircuit
from bode_plot import BodePlotCanvas
from time_response_plot import TimeResponseCanvas


class CircuitCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(
            QGraphicsView.ViewportUpdateMode.FullViewportUpdate
        )

        self.setSceneRect(0, 0, 800, 250)

        # Components
        self.resistor = ResistorItem(100)
        self.resistor.setPos(50, 40)
        self.scene.addItem(self.resistor)

        self.inductor = InductorItem(10)
        self.inductor.setPos(250, 40)
        self.scene.addItem(self.inductor)

        self.capacitor = CapacitorItem(10)
        self.capacitor.setPos(450, 40)
        self.scene.addItem(self.capacitor)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RLC Transfer Function Analyzer")

        self.canvas = CircuitCanvas()
        self.bode_plot = BodePlotCanvas()
        self.time_plot = TimeResponseCanvas()

        self.analyze_btn = QPushButton("Analyze Circuit")
        self.analyze_btn.clicked.connect(self.analyze)

        self.tf_label = QLabel("Transfer Function H(s) will appear here")
        self.tf_label.setFont(QFont("Consolas", 11))
        self.tf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tf_label.setStyleSheet(
            "border: 1px solid #aaa; padding: 8px; background: #f9f9f9;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.tf_label)
        layout.addWidget(self.bode_plot)
        layout.addWidget(self.time_plot)

        self.setLayout(layout)

    def analyze(self):
        R = self.canvas.resistor.value
        L = self.canvas.inductor.value
        C = self.canvas.capacitor.value

        circuit = RLCCircuit(R, L, C)
        H = circuit.transfer_function()

        # Show transfer function
        self.tf_label.setText(
            "Transfer Function H(s):\n\n" + str(H)
        )

        # Update plots
        self.bode_plot.plot(R, L, C)
        self.time_plot.plot_step_response(R, L, C)

        print("\n=== RLC ANALYSIS ===")
        print(f"R={R} Ω, L={L} mH, C={C} µF")
        print("H(s) =", H)
        print("====================\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(950, 900)
    window.show()
    sys.exit(app.exec())
import sys
from PyQt6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene,
    QPushButton, QVBoxLayout, QWidget, QLabel
)
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtCore import Qt

from resistor import ResistorItem
from capacitor import CapacitorItem
from inductor import InductorItem
from circuit_model import RLCCircuit
from bode_plot import BodePlotCanvas
from time_response_plot import TimeResponseCanvas


class CircuitCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(
            QGraphicsView.ViewportUpdateMode.FullViewportUpdate
        )

        self.setSceneRect(0, 0, 800, 250)

        # Components
        self.resistor = ResistorItem(100)
        self.resistor.setPos(50, 40)
        self.scene.addItem(self.resistor)

        self.inductor = InductorItem(10)
        self.inductor.setPos(250, 40)
        self.scene.addItem(self.inductor)

        self.capacitor = CapacitorItem(10)
        self.capacitor.setPos(450, 40)
        self.scene.addItem(self.capacitor)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RLC Transfer Function Analyzer")

        self.canvas = CircuitCanvas()
        self.bode_plot = BodePlotCanvas()
        self.time_plot = TimeResponseCanvas()

        self.analyze_btn = QPushButton("Analyze Circuit")
        self.analyze_btn.clicked.connect(self.analyze)

        self.tf_label = QLabel("Transfer Function H(s) will appear here")
        self.tf_label.setFont(QFont("Consolas", 11))
        self.tf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tf_label.setStyleSheet(
            "border: 1px solid #aaa; padding: 8px; background: #f9f9f9;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.tf_label)
        layout.addWidget(self.bode_plot)
        layout.addWidget(self.time_plot)

        self.setLayout(layout)

    def analyze(self):
        R = self.canvas.resistor.value
        L = self.canvas.inductor.value
        C = self.canvas.capacitor.value

        circuit = RLCCircuit(R, L, C)
        H = circuit.transfer_function()

        # Show transfer function
        self.tf_label.setText(
            "Transfer Function H(s):\n\n" + str(H)
        )

        # Update plots
        self.bode_plot.plot(R, L, C)
        self.time_plot.plot_step_response(R, L, C)

        print("\n=== RLC ANALYSIS ===")
        print(f"R={R} Ω, L={L} mH, C={C} µF")
        print("H(s) =", H)
        print("====================\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(950, 900)
    window.show()
    sys.exit(app.exec())
