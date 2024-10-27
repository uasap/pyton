# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Устанавливаем название окна
        self.setWindowTitle("ETL Data Fusion")

        # Связываем кнопки с функциями
        self.ui.btnLoadFiles.clicked.connect(self.load_files)  # Кнопка для загрузки файлов
        self.ui.btnRunDag.clicked.connect(self.run_dag)  # Кнопка для запуска DAG

        # Переменные для хранения данных
        self.booking_df = None
        self.client_df = None
        self.hotel_df = None
        self.merged_df = None

    def load_files(self):
        try:
            # Загрузка файла booking.csv
            booking_file, _ = QFileDialog.getOpenFileName(self, "Загрузить booking.csv", "", "CSV Files (*.csv)")
            if booking_file:
                self.booking_df = pd.read_csv(booking_file)

            # Загрузка файла client.csv
            client_file, _ = QFileDialog.getOpenFileName(self, "Загрузить client.csv", "", "CSV Files (*.csv)")
            if client_file:
                self.client_df = pd.read_csv(client_file)

            # Загрузка файла hotel.csv
            hotel_file, _ = QFileDialog.getOpenFileName(self, "Загрузить hotel.csv", "", "CSV Files (*.csv)")
            if hotel_file:
                self.hotel_df = pd.read_csv(hotel_file)

            # Отображение статуса загрузки
            self.ui.textEditStatus.append("Файлы успешно загружены!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при загрузке файлов: {e}")

    def run_dag(self):
        try:
            if self.booking_df is None or self.client_df is None or self.hotel_df is None:
                QMessageBox.warning(self, "Внимание", "Сначала загрузите все файлы!")
                return

            # Объединение данных
            self.merged_df = self.booking_df.merge(self.client_df, on="client_id").merge(self.hotel_df, on="hotel_id")

            # Приведение даты к единому формату
            if 'date' in self.merged_df.columns:
                self.merged_df['date'] = pd.to_datetime(self.merged_df['date'], errors='coerce')

            # Удаление невалидных колонок
            self.merged_df.dropna(axis=1, how='all', inplace=True)

            # Приведение валют к единому виду
            if 'exchange_rate' in self.merged_df.columns:
                self.merged_df['price'] = self.merged_df['price'] * self.merged_df['exchange_rate']
                self.merged_df.drop(columns=['exchange_rate'], inplace=True)

            # Отображение статуса
            self.ui.textEditStatus.append("Трансформация завершена!")

            # Заполнение tableData данными из объединенной таблицы
            self.display_data_in_table(self.merged_df)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при запуске DAG: {e}")

    def display_data_in_table(self, dataframe):
        # Создание модели для QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(dataframe.columns)

        # Заполнение модели данными из DataFrame
        for row in dataframe.itertuples(index=False):
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        # Установка модели в QTableView
        self.ui.tableData.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
