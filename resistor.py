from PyQt6.QtWidgets import QGraphicsItem, QInputDialog
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtCore import QRectF, Qt


class ResistorItem(QGraphicsItem):
    def __init__(self, value=10):
        super().__init__()
        self.value = value

        # 🔴 Bigger than drawing (IMPORTANT)
        self.width = 100
        self.height = 50

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

        painter.drawLine(0, symbol_y, 15, symbol_y)
        painter.drawLine(self.width - 15, symbol_y, self.width, symbol_y)

        x = 15
        step = 10
        zigzag_height = 6

        for i in range(6):
            if i % 2 == 0:
                painter.drawLine(x, symbol_y,
                                 x + step, symbol_y - zigzag_height)
            else:
                painter.drawLine(x, symbol_y,
                                 x + step, symbol_y + zigzag_height)
            x += step

        painter.setFont(QFont("Arial", 9))
        painter.drawText(
            0, text_y, self.width, 12,
            Qt.AlignmentFlag.AlignCenter,
            f"{self.value} Ω"
        )

    def mouseDoubleClickEvent(self, event):
        new_value, ok = QInputDialog.getDouble(
            None, "Edit Resistance",
            "Resistance (Ohms):",
            self.value, 0.1, 1e6, 2
        )

        if ok:
            self.value = new_value
            self.update()

        super().mouseDoubleClickEvent(event)
