from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtCore import Qt


class TerminalItem(QGraphicsEllipseItem):
    RADIUS = 5

    def __init__(self, x, y):
        super().__init__(
            -self.RADIUS, -self.RADIUS,
            2 * self.RADIUS, 2 * self.RADIUS
        )

        # Position relative to parent (component)
        self.setPos(x, y)

        # Logical node ID (used later for nodal analysis)
        self.node_id = None

        self.setBrush(QBrush(Qt.GlobalColor.white))
        self.setPen(QPen(Qt.GlobalColor.black, 1))

        self.setFlags(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable
        )
