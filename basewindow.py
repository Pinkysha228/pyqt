from PyQt5.QtWidgets import QWidget


class BaseWindow(QWidget):
    def __init__(self, header: str) -> None:
        super().__init__()
        self.setWindowTitle(header)
        self.setMinimumWidth(250)
        self.setFixedSize(400, 300)
        with open('style.css', 'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())