# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QHeaderView, QTableWidget
from PySide6.QtCore import Signal, Qt, QAbstractItemModel, QModelIndex
from PySide6.QtSql import QSqlDatabase as database
from PySide6.QtSql import QSqlQuery
from PySide6.QtGui import QPalette, QColor
import dark_palette
from datetime import date
darktheme_fix = QPalette()

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_AnaEkran

class NonDraggableHeader(QHeaderView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        # Ignore mouse press events to prevent dragging initiation
        event.ignore()  # This ensures the event doesn't propagate further

    def mouseMoveEvent(self, event):
        # Ignore mouse move events to prevent dragging
        event.ignore()
    def mouseDoubleClickEvent(self, event):
        # Ignore double-click events to prevent minimization
        event.ignore()

class NonResizableVerticalHeader(QHeaderView):
    def __init__(self, parent=None):
        super().__init__(parent)



    def mouseMoveEvent(self, event):
        # Ignore mouse move events to prevent dragging
        event.ignore()
    def mouseDoubleClickEvent(self, event):
        # Ignore double-click events to prevent minimization
        event.ignore()


class MainWindow(QWidget):
    page_switch_clicked = Signal(int)  # Custom signal with an integer argument


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AnaEkran()
        self.ui.setupUi(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Allow user to resize columns manually
        self.ui.tableWidget.horizontalHeader().setSectionsMovable(False)
        self.ui.tableWidget.horizontalHeader().setDragEnabled(True)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        # normally, get the array of the avaliable uruns, and add them via "addItems"
        #AVOID!!! "Tümü" should be the first element of the array ALWAYS
        #TODO: append to an array only containing "Tümü"
        urun_items = ["Tümü", "Option B", "Option C"]
        #self.ui.comboBox_urun.addItems(urun_items)
        #to make it currentText, you need to make it editable
        #self.ui.comboBox_urun.setCurrentIndex(0)
        #self.ui.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        horizontal_header = NonDraggableHeader(Qt.Horizontal)
        vertical_header = NonResizableVerticalHeader(Qt.Vertical)
        #self.ui.tableWidget.setHorizontalHeader(horizontal_header)
        #self.ui.tableWidget.setVerticalHeader(vertical_header)



        #set date
        #self.ui.dateEdit_3.setDate(date.today())


        #self.page_switch_clicked.connect(self.on_page_switch_clicked)
        #self.ui.pushButton_aramaVeSatis.clicked.connect(self.on_arama_ve_satis_clicked)
        #self.ui.pushButton_aboneler.clicked.connect(self.on_aboneler_clicked)

        db = database.addDatabase("QSQLITE")
        db.setDatabaseName("tupsu.db")

        if not db.open():
          print("Error opening database:", db.lastError().text())
          exit()

        print(db)

        table_name = "urunler"

        query = QSqlQuery(db)
        query.exec_(f"SELECT * FROM {table_name}")  # Using f-string for clarity

        print("queryyy")
        print(query.isValid)


        if not query.isValid():
          print("Error executing query:", query.lastError().text())
        else:
          # Process each row (assuming query is valid)
          while query.next():
            try:
              # Access column values using their names or index (carefully!)
              id = query.value("id").toInt()  # Assuming 'id' column exists
              username = query.value("urun_adi").toString()
              # ... access other columns if present
              print(f"ID: {id}, Username: {username}")  # Example output formatting
            except TypeError as e:
              print(f"Error accessing data: {e}")  # Handle potential type mismatches



    def on_page_switch_clicked(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def on_arama_ve_satis_clicked(self):
        self.page_switch_clicked.emit(1)  # 1 == Arama ve satislar

    def on_aboneler_clicked(self):
        self.page_switch_clicked.emit(0)

    def limitColumnResize(self, logicalIndex, oldSize, newSize):
        # Get the width of the screen
        screen_width = self.table_widget.viewport().width()

        # Check if the resized column exceeds the screen width
        if self.table_widget.horizontalHeader().length() > screen_width:
            self.table_widget.horizontalHeader().resizeSection(logicalIndex, oldSize)

    def highlight_row(self, row):
        for col in range(self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, col)
            if item:
                item.setBackground(QColor('green'))
                item.setData(Qt.BackgroundRole, QColor('green'))





with open('MaterialDark.qss', 'r') as f:
    stylesheet = f.read()


if __name__ == "__main__":
    #qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    #palette = qdarktheme.load_palette(theme="dark")
    app.setPalette(dark_palette.PALETTE_DARK)

    #qdarktheme.setup_theme()
    widget = MainWindow()
    #app.setStyleSheet(stylesheet)
    widget.show()
    sys.exit(app.exec())
