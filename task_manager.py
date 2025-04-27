import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QListWidget
from basewindow import BaseWindow
import random

class TaskListWidget(BaseWindow):
    def __init__(self) -> None:
        super().__init__('Task Manager')
        self.init_ui()

    def init_ui(self) -> None:
        self.layout = QVBoxLayout() 

        self.task_input = QLineEdit(self)
        self.add_button = QPushButton('Додати задачу', self)
        self.add_button.clicked.connect(self.add_task)
        self.task_list = QListWidget(self)
        self.delete_button = QPushButton("Видалити задачу", self)
        self.delete_button.clicked.connect(self.delete_task)
        self.delete_button.setObjectName('deleteButton')


        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

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


app = QApplication(sys.argv)
window = TaskListWidget()
window.show()
sys.exit(app.exec_())