import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QComboBox,
                             QBoxLayout, QListWidget, QMenu)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from basewindow import BaseWindow
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, chart_header: str, width: int = 5, height: int = 4, dpi: int = 80) -> None:
        self.fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MatplotlibCanvas, self).__init__(self.fig)
        self.chart_header = chart_header
        self.update_plot()
    def update_plot(self, data: list = None) -> None:
        self.axes.clear()
        labels = []
        values = []
        if data is not None:
            for expense in data:
                category = expense['category']
                value = expense['value']
                if category not in labels:
                    labels.append(category)
                    values.append(value)
                else:
                    values[labels.index(category)] += value
        else:
            labels = ['Empty']
            values = [1]
        self.axes.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        self.axes.axis('equal')
        self.axes.set_title(self.chart_header, fontdict={'fontsize': 15})
        self.draw()
class ExpenseTrackerApp(BaseWindow):
    def __init__(self) -> None:
        super().__init__("Expense Tracker")
        self.categories = ['Їжа', 'Транспорт', 'Спорт', 'Розваги', 'Аптека', 'Кредит', 'Казіно','Інше']
        self.DATA = []
        layout = QVBoxLayout()
        layout.addLayout(self.init_header_layout())
        layout.addLayout(self.init_main_layout())
        self.setLayout(layout)
    def init_header_layout(self) -> QBoxLayout:
        header_layout = QHBoxLayout()
        self.money_input = QLineEdit(self)
        self.money_input.setPlaceholderText("Ціна")
        self.expense_name_input = QLineEdit(self)
        self.expense_name_input.setPlaceholderText("Опис")
        self.expense_category_combobox = QComboBox(self)
        self.expense_category_combobox.addItems(self.categories)
        self.add_expense_button = QPushButton("Додати витрату", self)
        self.add_expense_button.clicked.connect(self.add_expense)
        header_layout.addWidget(self.money_input)
        header_layout.addWidget(self.expense_name_input)
        header_layout.addWidget(self.expense_category_combobox)
        header_layout.addWidget(self.add_expense_button)
        return header_layout
    def init_main_layout(self) -> QBoxLayout:
        main_layout = QHBoxLayout()
        self.expense_list_widget = QListWidget(self)
        self.graph = MatplotlibCanvas("Expenses", width=4, height=4)
        main_layout.addWidget(self.expense_list_widget)
        main_layout.addWidget(self.graph)
        return main_layout
    def add_expense(self) -> None:
        category = self.expense_category_combobox.currentText()
        description = self.expense_name_input.text()
        if len(description) > 14:
            description = description[:14] + "..."
        try:
            value = float(self.money_input.text())
        except ValueError:
            self.show_modal('Ой', 'Щось пішло не так', 2)
        self.DATA.append({
            "category": category,
            "description": description,
            "value": value
        })
        self.graph.update_plot(self.DATA)
        self.update_list()
        self.clear_inputs()

    def update_list(self):
        self.expense_list_widget.clear()
        for expense in self.DATA:
            self.expense_list_widget.addItem(f'{expense['category']}: ${expense["value"]} | {expense["description"]}')

    def clear_inputs(self):
        self.money_input.clear()
        self.expense_name_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTrackerApp()
    window.show()
    sys.exit(app.exec_())
