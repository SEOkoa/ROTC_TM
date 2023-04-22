# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_MembersoPIIcN.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHeaderView, QLayout, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_EditMembers_dialog(object):
    def setupUi(self, EditMembers_dialog):
        if not EditMembers_dialog.objectName():
            EditMembers_dialog.setObjectName(u"EditMembers_dialog")
        EditMembers_dialog.resize(818, 480)
        self.gridLayout_3 = QGridLayout(EditMembers_dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(EditMembers_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)

        self.btn_addrow = QPushButton(self.frame)
        self.btn_addrow.setObjectName(u"btn_addrow")

        self.verticalLayout.addWidget(self.btn_addrow)

        self.btn_removerow = QPushButton(self.frame)
        self.btn_removerow.setObjectName(u"btn_removerow")

        self.verticalLayout.addWidget(self.btn_removerow)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_2 = QFrame(EditMembers_dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Member_Edit = QWidget()
        self.Member_Edit.setObjectName(u"Member_Edit")
        self.gridLayout_2 = QGridLayout(self.Member_Edit)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.tableWidget = QTableWidget(self.Member_Edit)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Member_Edit)
        self.Member_list = QWidget()
        self.Member_list.setObjectName(u"Member_list")
        self.gridLayout = QGridLayout(self.Member_list)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listView = QListView(self.Member_list)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Member_list)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(EditMembers_dialog)
        self.btn_save.clicked.connect(EditMembers_dialog.accept)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EditMembers_dialog)
    # setupUi

    def retranslateUi(self, EditMembers_dialog):
        EditMembers_dialog.setWindowTitle(QCoreApplication.translate("EditMembers_dialog", u"\uba85\ub2e8 \uc218\uc815", None))
        self.btn_save.setText(QCoreApplication.translate("EditMembers_dialog", u"\uc800\uc7a5", None))
        self.btn_addrow.setText(QCoreApplication.translate("EditMembers_dialog", u"\ud589 \ucd94\uac00", None))
        self.btn_removerow.setText(QCoreApplication.translate("EditMembers_dialog", u"\ud589 \uc0ad\uc81c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EditMembers_dialog", u"\uae30\uc218", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EditMembers_dialog", u"\ub2e8\ubc88(\uad50\ub0b4)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EditMembers_dialog", u"\ub2e8\ubc88(\uc804\uc0b0)", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EditMembers_dialog", u"\uc774\ub984", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EditMembers_dialog", u"\uc131\ubcc4(M/F)", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EditMembers_dialog", u"\uc804\ud654\ubc88\ud638", None));
    # retranslateUi

