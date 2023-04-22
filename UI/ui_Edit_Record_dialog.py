# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_Record_dialogTrCRMz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Record_dialog(object):
    def setupUi(self, Record_dialog):
        if not Record_dialog.objectName():
            Record_dialog.setObjectName(u"Record_dialog")
        Record_dialog.resize(671, 511)
        self.gridLayout = QGridLayout(Record_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(Record_dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 50):
            self.tableWidget.setRowCount(50)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(50)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(Record_dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Record_dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.retranslateUi(Record_dialog)

        QMetaObject.connectSlotsByName(Record_dialog)
    # setupUi

    def retranslateUi(self, Record_dialog):
        Record_dialog.setWindowTitle(QCoreApplication.translate("Record_dialog", u"\uccb4\ub825\uce21\uc815 \uae30\ub85d", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Record_dialog", u"\uc774\ub984", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Record_dialog", u"Push-Up", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Record_dialog", u"Sit-Up", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Record_dialog", u"\ub700\uac78\uc74c(3km)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Record_dialog", u"\ub4f1\uae09", None));
        self.pushButton.setText(QCoreApplication.translate("Record_dialog", u"\uc800\uc7a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("Record_dialog", u"\ucde8\uc18c", None))
    # retranslateUi

