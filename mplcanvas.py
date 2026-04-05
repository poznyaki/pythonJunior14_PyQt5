import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, data_dict, parent=None, width=5, height=4, dpi=100):
        # Створюємо фігуру та осі
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        super().__init__(self.fig)

        # Малюємо діаграму при ініціалізації
        self.plot_pie(data_dict)

    def plot_pie(self, data):
        self.axes.clear()

        labels = list(data.keys())
        values = list(data.values())

        # Створення кругової діаграми
        # autopct='%1.1f%%' виводить відсотки з одним знаком після коми
        self.axes.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        self.axes.set_title("Статистика заповнення")

        self.draw()


# --- Блок для запуску вікна ---

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib Pie Chart у PyQt5")

        # Наш словник з даними
        stats = {
            'Виконано': 45.5,
            'В процесі': 30.0,
            'Очікує': 15.5,
            'Помилки': 9.0
        }

        # Створюємо віджет полотна
        sc = MatplotlibCanvas(stats, width=6, height=5, dpi=100)

        # Розміщуємо полотно у вікні
        layout = QVBoxLayout()
        layout.addWidget(sc)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())