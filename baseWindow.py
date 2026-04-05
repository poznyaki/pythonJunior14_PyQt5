from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

class BaseWindow(QWidget):
    def __init__(self, header: str, size_x: int = 400, size_y: int = 300) -> None:
        super().__init__()
        self.setWindowTitle(header)
        self.setWindowIcon(QIcon("magic_ball/magic-8-ball.svg"))
        self.setFixedSize(size_x, size_y)

        with open('style.qss', 'r') as css:
            self.setStyleSheet(css.read())
