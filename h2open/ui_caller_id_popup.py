# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caller_id_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_ArayanPopup(object):
    def setupUi(self, ArayanPopup):
        if not ArayanPopup.objectName():
            ArayanPopup.setObjectName(u"ArayanPopup")
        ArayanPopup.resize(686, 492)
        self.label = QLabel(ArayanPopup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 81, 18))
        self.label_2 = QLabel(ArayanPopup)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 30, 101, 18))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)

        self.retranslateUi(ArayanPopup)

        QMetaObject.connectSlotsByName(ArayanPopup)
    # setupUi

    def retranslateUi(self, ArayanPopup):
        ArayanPopup.setWindowTitle(QCoreApplication.translate("ArayanPopup", u"Abone Bilgileri (Caller ID)", None))
        self.label.setText(QCoreApplication.translate("ArayanPopup", u"Arayan No:", None))
        self.label_2.setText(QCoreApplication.translate("ArayanPopup", u"05322976326", None))
    # retranslateUi

