from PyQt6.QtWidgets import QGraphicsItem, QInputDialog
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtCore import QRectF, Qt


class CapacitorItem(QGraphicsItem):
    def __init__(self, value=10.0):
        super().__init__()
        self.value = value  # µF

        # 🔴 Bigger bounding box prevents ghosting
        self.width = 80
        self.height = 50

        # 🔴 Disable caching (IMPORTANT)
        self.setCacheMode(QGraphicsItem.CacheMode.NoCache)

        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.GlobalColor.black, 2))

        symbol_y = 20
        text_y = 38

        # Wires
        painter.drawLine(0, symbol_y, 25, symbol_y)
        painter.drawLine(self.width - 25, symbol_y,
                         self.width, symbol_y)

        # Capacitor plates
        painter.drawLine(25, symbol_y - 10, 25, symbol_y + 10)
        painter.drawLine(self.width - 25, symbol_y - 10,
                         self.width - 25, symbol_y + 10)

        # Text
        painter.setFont(QFont("Arial", 9))
        painter.drawText(
            0, text_y, self.width, 12,
            Qt.AlignmentFlag.AlignCenter,
            f"{self.value} µF"
        )

    def mouseDoubleClickEvent(self, event):
        new_value, ok = QInputDialog.getDouble(
            None,
            "Edit Capacitance",
            "Capacitance (µF):",
            self.value,
            0.01,
            1_000_000,
            2
        )

        if ok:
            self.value = new_value
            self.update()

        super().mouseDoubleClickEvent(event)
