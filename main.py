import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QListWidget, \
    QFileDialog, QTextEdit, QLabel, QLineEdit, QFormLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение PyQt")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tab Widget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_tab1(), "Сканировать папку")
        self.tabs.addTab(self.create_tab2(), "Редактировать файл")
        self.tabs.addTab(self.create_tab3(), "Сохранить текст")
        self.tabs.addTab(self.create_tab4(), "Форма с элементами")
        self.tabs.addTab(self.create_tab5(), "Чтение списка")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        central_widget.setLayout(layout)

    # Первая вкладка - сканировать папку
    def create_tab1(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.file_list_widget = QListWidget()
        scan_button = QPushButton("Выбрать папку")
        scan_button.clicked.connect(self.scan_folder)

        layout.addWidget(scan_button)
        layout.addWidget(self.file_list_widget)
        tab.setLayout(layout)

        return tab

    def scan_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if folder_path:
            self.file_list_widget.clear()
            for file_name in os.listdir(folder_path):
                self.file_list_widget.addItem(file_name)

    # Вторая вкладка - редактировать файл
    def create_tab2(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        open_file_button = QPushButton("Открыть файл")
        open_file_button.clicked.connect(self.open_file)

        layout.addWidget(open_file_button)
        layout.addWidget(self.text_edit)
        tab.setLayout(layout)

        return tab

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.text_edit.setText(f.read())

    # Третья вкладка - сохранить текст в файл
    def create_tab3(self):
        tab = QWidget()
        layout = QVBoxLayout()

        save_button = QPushButton("Сохранить текст")
        save_button.clicked.connect(self.save_text)

        layout.addWidget(self.text_edit)
        layout.addWidget(save_button)
        tab.setLayout(layout)

        return tab

    def save_text(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.text_edit.toPlainText())

    # Четвертая вкладка - форма с элементами
    def create_tab4(self):
        tab = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.line_edit4 = QLineEdit()
        self.line_edit5 = QLineEdit()

        form_layout.addRow("Поле 1:", self.line_edit1)
        form_layout.addRow("Поле 2:", self.line_edit2)
        form_layout.addRow("Поле 3:", self.line_edit3)
        form_layout.addRow("Поле 4:", self.line_edit4)
        form_layout.addRow("Поле 5:", self.line_edit5)

        save_button = QPushButton("Сохранить данные")
        save_button.clicked.connect(self.save_form_data)

        layout.addLayout(form_layout)
        layout.addWidget(save_button)
        tab.setLayout(layout)

        return tab

    def save_form_data(self):
        data = {
            "Поле 1": self.line_edit1.text(),
            "Поле 2": self.line_edit2.text(),
            "Поле 3": self.line_edit3.text(),
            "Поле 4": self.line_edit4.text(),
            "Поле 5": self.line_edit5.text(),
        }
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить данные", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'a', encoding='utf-8') as f:
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")

    # Пятая вкладка - чтение списка
    def create_tab5(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.result_label = QLabel("Результат:")
        open_list_button = QPushButton("Открыть список")
        open_list_button.clicked.connect(self.open_list_file)

        layout.addWidget(open_list_button)
        layout.addWidget(self.result_label)
        tab.setLayout(layout)

        return tab

    def open_list_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.result_label.setText(f"Поле 2: {lines[1].strip()}")


# Запуск приложения
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
