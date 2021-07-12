import sys
from PyQt5 import QtWidgets
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_mainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_2.clicked.connect(self.add_task)

    def save(self):
        pass

    def add_task(self):
        # получение значения поля
        all_inputs = self.lineEdit.text() and self.lineEdit_2.text()
        if all_inputs:
            print('Valid')
        else:
            print('Not valid!')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
