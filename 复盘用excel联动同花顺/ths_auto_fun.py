import json
import os
from tkinter import Tk, filedialog
import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView, QAbstractItemView, \
    QTableWidget
from ths_auto_ui import Ui_Form
from ths_link import send_code_message
def write_config(k, v):
    file = open('config.json', 'r+', encoding='utf-8')
    data = json.load(file)
    data[k] = v
    file.close()
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
        f.close()


class THS_AUTO(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
                            QtCore.Qt.WindowCloseButtonHint |  # 使能关闭按钮
                            QtCore.Qt.WindowStaysOnTopHint)  # 窗体总在最前端
        self.read_config()

        self.pushButton.clicked.connect(self.get_excel_path)
        self.pushButton_2.clicked.connect(self.get_exe_path)

        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.get_data()

        self.tableWidget.verticalHeader().setHidden(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.itemSelectionChanged.connect(self.item_click_event)    # 表格点击事件
        self.tableWidget.setSortingEnabled(True)  # 启用排序功能

    def item_click_event(self):
        exe_name = os.path.basename(self.lineEdit_2.text())
        selected_rows = set()
        for item in self.tableWidget.selectedItems():
            selected_rows.add(item.row())

        selected_data = []
        for row in selected_rows:
            # []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                selected_data.append(item.text())
        print(selected_data)
        send_code_message(selected_data[1], exe_name)

    def read_config(self):
        # 读取json文件
        if os.path.exists('config.json') is False:
            data = {"excel_file": "", "ths_exe": ""}
            with open('config.json', 'w') as f:
                json.dump(data, f)
                f.close()
        f = open('config.json', 'r')
        data = json.load(f)
        self.lineEdit.setText(data.get('excel_file'))
        self.lineEdit_2.setText(data.get('ths_exe'))

    def get_excel_path(self):
        root = Tk()
        root.withdraw()  # 隐藏主窗口

        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")],
                                               title="选择Excel文件")
        self.lineEdit.setText(file_path)
        self.get_data()
        write_config('excel_file', file_path)

    def get_exe_path(self):
        root = Tk()
        root.withdraw()  # 隐藏主窗口

        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe"), ("All files", "*.*")],
                                               title="选择同花顺EXE文件")
        self.lineEdit_2.setText(file_path)
        write_config('ths_exe', file_path)

    def get_data(self):
        # 读取Excel文件
        try:
            df = pd.read_excel(self.lineEdit.text(), skiprows=1, dtype={'代码': str})
            df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
            result = df.iloc[0:]
            self.tableWidget.setColumnCount(len(result.columns))
            self.tableWidget.setRowCount(len(result))

            # 设置表头
            self.tableWidget.setHorizontalHeaderLabels(result.columns)

            # 填充数据
            for row in range(len(result)):
                for col in range(len(result.columns)):
                    item = QTableWidgetItem(str(result.iloc[row, col]))
                    if col == len(result.columns) - 1:
                        # 以数值方式显示，方便排序
                        item.setData(QtCore.Qt.DisplayRole, float(round(result.iloc[row, col] * 100, 2)))
                    else:
                        # 文本方式显示
                        item.setText(str(result.iloc[row, col]))
                    self.tableWidget.setItem(row, col, item)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    window = THS_AUTO()
    window.show()
    app.exec()
