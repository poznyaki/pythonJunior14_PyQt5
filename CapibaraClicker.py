import sys
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QLabel,
                             QPushButton, QApplication, )
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CapibaraClicker(QWidget):
    def __init__(self):
        super().__init__()

        self.coins = 0
        self.click_power = 1
        self.upgrade_cost = 10

        self.setWindowTitle("Capibara Clicker")
        self.resize(400, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Заклікай капібару!")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.title_label)

        self.coins_label = QLabel("Монети: 0")
        self.coins_label.setAlignment(Qt.AlignCenter)
        self.coins_label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.coins_label)

        self.click_button = QPushButton("Клікай 🦫 Мене")
        self.click_button.setFont(QFont("Arial", 20))
        self.click_button.clicked.connect(self.click_capibara)
        self.layout.addWidget(self.click_button)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.info_label)

        self.upgrade_button = QPushButton("Прокачати клік (10)")
        self.upgrade_button.setFont(QFont("Arial", 12))
        self.upgrade_button.clicked.connect(self.buy_upgrade)
        self.layout.addWidget(self.upgrade_button)

    def click_capibara(self):
        print("На мене клікнули")
        self.coins += self.click_power
        self.update_labels()

    def buy_upgrade(self):
        if self.coins >= self.upgrade_cost:
            self.coins -= self.upgrade_cost
            self.click_power += 1
            self.upgrade_cost += 10
            self.info_label.setText("Прокачка успішна!")
        else:
            self.info_label.setText("Недостатньо монет!")
        self.update_labels()
#new.codeshare.io/333333
    def update_labels(self):
        self.coins_label.setText(f"Монети: {self.coins}")
        self.upgrade_button.setText(f"Прокачати клік ({self.upgrade_cost})")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("capibara.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = CapibaraClicker()
    window.show()
    sys.exit(app.exec_())