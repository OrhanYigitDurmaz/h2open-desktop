# This Python file uses the following encoding: utf-8

from PySide6.QtSql import QSqlDatabase as database
from PySide6.QtWidgets import QMessageBox

def connect_database():
    db = database.addDatabase('QODBC')
    db.setDatabaseName("h2open_maria")

    if not db.open():
      error_message = db.lastError().text()
      QMessageBox.critical(None, "Database Connection", f"Database Connection Failed!\nError: {error_message}")
      exit()


# if __name__ == "__main__":
#     pass
