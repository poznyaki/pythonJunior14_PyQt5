import sys
from PyQt5.QtWidgets import (QVBoxLayout,
                             QLineEdit,
                             QPushButton,
                             QListWidget,
                             QApplication,
                             QHBoxLayout,
                             QComboBox)
from baseWindow import BaseWindow
import matplotlib.pyplot as plt
from mplcanvas import MatplotlibCanvas

class ExpenseTracker(BaseWindow):
    def __init__(self):
        super().__init__("ExpenseTrackerApp", 800, 600)
        self.categories = ["food", "transport", "bills", "shopping", "other"]
        self.DATA = []
        layout = QVBoxLayout()

        layout.addLayout(self.init_header_layout())
        layout.addLayout(self.init_main_layout())
        self.setLayout(layout)

    def init_header_layout(self):
        header_layout = QHBoxLayout()
        self.money_input = QLineEdit(self)
        self.expense_name_input = QLineEdit(self)
        self.category_combobox = QComboBox(self)
        self.category_combobox.addItems(self.categories)
        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add_expense)

        header_layout.addWidget(self.money_input)
        header_layout.addWidget(self.expense_name_input)
        header_layout.addWidget(self.category_combobox)
        header_layout.addWidget(self.add_button)
        return header_layout

    def init_main_layout(self):
        main_layout = QHBoxLayout()
        self.list_widget = QListWidget()
        self.graph = MatplotlibCanvas({"Test" : 25, "Test2" : 30})
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.graph)
        return main_layout

    def add_expense(self) -> None:
        category_name = self.category_combobox.currentText()
        description = self.expense_name_input.text()
        if len(description) > 14:
            description = description[:14] + "..."
        try:
            value = float(self.money_input.text())
        except ValueError:
            # TODO: додати модальне вікно
            return
        self.DATA.append({
         category_name : value,
        })
        self.graph.update_data(self.DATA)

    def update_expense(self) -> None:
        self.list_widget.clear()
        for expense in self.DATA:
            self.list_widget.addItem(expense)

    def clear_input(self):
        self.money_input.clear()
        self.expense_name_input.clear()

def main():
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
