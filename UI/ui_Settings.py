# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsqeLmdK.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Settings_dialog(object):
    def setupUi(self, Settings_dialog):
        if not Settings_dialog.objectName():
            Settings_dialog.setObjectName(u"Settings_dialog")
        Settings_dialog.resize(640, 480)
        self.gridLayout = QGridLayout(Settings_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Settings_dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(Settings_dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Settings_dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Settings_dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(Settings_dialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.label_4 = QLabel(Settings_dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(Settings_dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.label_2 = QLabel(Settings_dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.graphicsView = QGraphicsView(Settings_dialog)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.pushButton_3 = QPushButton(Settings_dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Settings_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Settings_dialog)
        self.buttonBox.accepted.connect(Settings_dialog.accept)
        self.buttonBox.rejected.connect(Settings_dialog.reject)

        QMetaObject.connectSlotsByName(Settings_dialog)
    # setupUi

    def retranslateUi(self, Settings_dialog):
        Settings_dialog.setWindowTitle(QCoreApplication.translate("Settings_dialog", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("Settings_dialog", u"\uc124\uc815", None))
        self.pushButton_2.setText(QCoreApplication.translate("Settings_dialog", u"\ud559\uad70\ub2e8 \uc815\ubcf4", None))
        self.pushButton.setText(QCoreApplication.translate("Settings_dialog", u"\uc790\ub3d9\uc800\uc7a5..", None))
        self.label.setText(QCoreApplication.translate("Settings_dialog", u"\ud559\uad50\uba85", None))
        self.textEdit.setHtml(QCoreApplication.translate("Settings_dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EX) \uba85\ubb38\uc0ac\ud559 \ud30c\uc774\ucc28\uc774 \ub2e4\uc774\uac00\ucfe0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Settings_dialog", u"\ud559\uad70\ub2e8 \ubc88\ud638", None))
        self.label_2.setText(QCoreApplication.translate("Settings_dialog", u"\uc0ac\uc6a9\ud560 \ud559\uad50 \ub9c8\ud06c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Settings_dialog", u"\ucc3e\uc544\ubcf4\uae30..", None))
    # retranslateUi

