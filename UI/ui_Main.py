# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainVoVVwJ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 694)
        self.actionView_AppInfo = QAction(MainWindow)
        self.actionView_AppInfo.setObjectName(u"actionView_AppInfo")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.btn_MemberManage = QPushButton(self.frame)
        self.btn_MemberManage.setObjectName(u"btn_MemberManage")

        self.verticalLayout.addWidget(self.btn_MemberManage)

        self.btn_TrainingManage = QPushButton(self.frame)
        self.btn_TrainingManage.setObjectName(u"btn_TrainingManage")

        self.verticalLayout.addWidget(self.btn_TrainingManage)

        self.btn_RecordManage = QPushButton(self.frame)
        self.btn_RecordManage.setObjectName(u"btn_RecordManage")

        self.verticalLayout.addWidget(self.btn_RecordManage)

        self.btn_SquadManage = QPushButton(self.frame)
        self.btn_SquadManage.setObjectName(u"btn_SquadManage")

        self.verticalLayout.addWidget(self.btn_SquadManage)

        self.btn_Inbody = QPushButton(self.frame)
        self.btn_Inbody.setObjectName(u"btn_Inbody")

        self.verticalLayout.addWidget(self.btn_Inbody)

        self.btn_PictureManage = QPushButton(self.frame)
        self.btn_PictureManage.setObjectName(u"btn_PictureManage")

        self.verticalLayout.addWidget(self.btn_PictureManage)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_setting = QPushButton(self.frame)
        self.btn_setting.setObjectName(u"btn_setting")

        self.verticalLayout.addWidget(self.btn_setting)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Page_MemberManage = QWidget()
        self.Page_MemberManage.setObjectName(u"Page_MemberManage")
        self.gridLayout = QGridLayout(self.Page_MemberManage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.Page_MemberManage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_NewMember = QPushButton(self.frame_3)
        self.btn_NewMember.setObjectName(u"btn_NewMember")

        self.verticalLayout_3.addWidget(self.btn_NewMember)

        self.btn_EditMember = QPushButton(self.frame_3)
        self.btn_EditMember.setObjectName(u"btn_EditMember")

        self.verticalLayout_3.addWidget(self.btn_EditMember)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.list_Memberlist = QListWidget(self.Page_MemberManage)
        self.list_Memberlist.setObjectName(u"list_Memberlist")

        self.gridLayout.addWidget(self.list_Memberlist, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page_MemberManage)
        self.Page_Training = QWidget()
        self.Page_Training.setObjectName(u"Page_Training")
        self.gridLayout_2 = QGridLayout(self.Page_Training)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_4 = QFrame(self.Page_Training)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.radio_3daystraining = QRadioButton(self.frame_4)
        self.radio_3daystraining.setObjectName(u"radio_3daystraining")

        self.horizontalLayout_4.addWidget(self.radio_3daystraining)

        self.radio_5daystraining = QRadioButton(self.frame_4)
        self.radio_5daystraining.setObjectName(u"radio_5daystraining")

        self.horizontalLayout_4.addWidget(self.radio_5daystraining)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.radio_include_attendance = QRadioButton(self.frame_4)
        self.radio_include_attendance.setObjectName(u"radio_include_attendance")

        self.horizontalLayout_3.addWidget(self.radio_include_attendance)

        self.radio_exclude_attendance = QRadioButton(self.frame_4)
        self.radio_exclude_attendance.setObjectName(u"radio_exclude_attendance")

        self.horizontalLayout_3.addWidget(self.radio_exclude_attendance)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.check_MakeHole = QCheckBox(self.frame_4)
        self.check_MakeHole.setObjectName(u"check_MakeHole")

        self.horizontalLayout_2.addWidget(self.check_MakeHole)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.DE_startdate = QDateEdit(self.frame_4)
        self.DE_startdate.setObjectName(u"DE_startdate")
        self.DE_startdate.setCalendarPopup(False)

        self.horizontalLayout_5.addWidget(self.DE_startdate)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.btn_TrainingPrint = QPushButton(self.frame_4)
        self.btn_TrainingPrint.setObjectName(u"btn_TrainingPrint")

        self.verticalLayout_6.addWidget(self.btn_TrainingPrint)


        self.gridLayout_2.addWidget(self.frame_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.Page_Training)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.Preview_Training = QTableView(self.Page_Training)
        self.Preview_Training.setObjectName(u"Preview_Training")

        self.gridLayout_2.addWidget(self.Preview_Training, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page_Training)
        self.Page_Record = QWidget()
        self.Page_Record.setObjectName(u"Page_Record")
        self.gridLayout_3 = QGridLayout(self.Page_Record)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_NewRecord = QPushButton(self.Page_Record)
        self.btn_NewRecord.setObjectName(u"btn_NewRecord")

        self.verticalLayout_7.addWidget(self.btn_NewRecord)

        self.btn_EditRecord = QPushButton(self.Page_Record)
        self.btn_EditRecord.setObjectName(u"btn_EditRecord")

        self.verticalLayout_7.addWidget(self.btn_EditRecord)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)


        self.gridLayout_3.addLayout(self.verticalLayout_7, 2, 1, 1, 1)

        self.list_Record = QListWidget(self.Page_Record)
        self.list_Record.setObjectName(u"list_Record")

        self.gridLayout_3.addWidget(self.list_Record, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page_Record)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addSeparator()
        self.menu_3.addAction(self.actionView_AppInfo)
        self.menu_3.addAction(self.actionhelp)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionView_AppInfo.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc815\ubcf4", None))
#if QT_CONFIG(shortcut)
        self.actionView_AppInfo.setShortcut(QCoreApplication.translate("MainWindow", u"R, Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9 \uc124\uba85\uc11c", None))
        self.btn_MemberManage.setText(QCoreApplication.translate("MainWindow", u"\uba85\ub2e8 \uad00\ub9ac", None))
        self.btn_TrainingManage.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ub825\ub2e8\ub828\uc77c\uc9c0", None))
        self.btn_RecordManage.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ub825\uce21\uc815\uae30\ub85d", None))
        self.btn_SquadManage.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc131\ud45c \uc791\uc131", None))
        self.btn_Inbody.setText(QCoreApplication.translate("MainWindow", u"\uc778\ubc14\ub514 \uae30\ub85d", None))
        self.btn_PictureManage.setText(QCoreApplication.translate("MainWindow", u"\uc99d\uba85\uc0ac\uc9c4 \uad00\ub9ac", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.btn_NewMember.setText(QCoreApplication.translate("MainWindow", u"\uc0c8\ub85c \ub9cc\ub4e4\uae30", None))
        self.btn_EditMember.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9d1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ub2e8 \uc77c\uc790", None))
        self.radio_3daystraining.setText(QCoreApplication.translate("MainWindow", u"\uc8fc 3\uc77c (\uc6d4\ud654\uc218)", None))
        self.radio_5daystraining.setText(QCoreApplication.translate("MainWindow", u"\uc8fc 5\uc77c ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\uc11d \ud655\uc778\ub780", None))
        self.radio_include_attendance.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud568", None))
        self.radio_exclude_attendance.setText(QCoreApplication.translate("MainWindow", u"\ube44\ud3ec\ud568", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud0c0\uacf5\ub77c\uc778", None))
        self.check_MakeHole.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud568 / \ube44\ud3ec\ud568", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\uc77c", None))
        self.btn_TrainingPrint.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\ub825", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\ub9ac\ubcf4\uae30", None))
        self.btn_NewRecord.setText(QCoreApplication.translate("MainWindow", u"\uc0c8\ub85c \ub9cc\ub4e4\uae30", None))
        self.btn_EditRecord.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9d1", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
    # retranslateUi

