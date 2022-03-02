import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
import random


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.pushButton.hide()
        self.flag = True
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.flag:
            self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        for i in range(10):
            x = random.randint(1, 664)
            y = random.randint(1, 401)
            r = random.randint(10, 100)
            qp.drawPoint(x, y)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
