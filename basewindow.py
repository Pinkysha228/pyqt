from PyQt5.QtWidgets import QWidget, QMessageBox


class BaseWindow(QWidget):
    def __init__(self, header: str) -> None:
        super().__init__()
        self.setWindowTitle(header)
        self.setMinimumWidth(250)
        self.setFixedSize(800, 600)
        with open('style.css', 'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())

    @staticmethod
    def show_modal(header: str, text: str, icon: int = 0):
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(text)
        match icon:
            case 0: msg.setIcon(QMessageBox.Information)
            case 1: msg.setIcon(QMessageBox.Warning)
            case 2: msg.setIcon(QMessageBox.Critical)
            case 3: msg.setIcon(QMessageBox.Question)
            case _: raise Exception('ваще та можна лише від 0 до 3')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
