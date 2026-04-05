import sys
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QListWidget, QApplication
from baseWindow import BaseWindow

class TasksWidget(BaseWindow):
    def __init__(self) -> None:
        super().__init__("TaskManager")
        self.init_ui()

    def init_ui(self) -> None:
        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.add_button = QPushButton("Add task", self)
        self.add_button.clicked.connect(self.add_task)
        self.task_list = QListWidget(self)
        self.delete_button = QPushButton("Delete selected task", self)
        self.delete_button.clicked.connect(self.delete_task)

        layout.addWidget(self.task_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()

    def delete_task(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            item_row = self.task_list.row(selected_item)
            self.task_list.takeItem(item_row)


def main():
    app = QApplication(sys.argv)
    window = TasksWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


