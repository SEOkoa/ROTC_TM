# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MemberList_Maker_dialogkenwdl.ui'
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
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Member_register_dialog(object):
    def setupUi(self, Member_register_dialog):
        if not Member_register_dialog.objectName():
            Member_register_dialog.setObjectName(u"Member_register_dialog")
        Member_register_dialog.resize(640, 464)
        self.verticalLayout = QVBoxLayout(Member_register_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Member_register_dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.TE_Grade = QTextEdit(Member_register_dialog)
        self.TE_Grade.setObjectName(u"TE_Grade")

        self.horizontalLayout.addWidget(self.TE_Grade)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(Member_register_dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.TE_Amount = QTextEdit(Member_register_dialog)
        self.TE_Amount.setObjectName(u"TE_Amount")

        self.horizontalLayout_3.addWidget(self.TE_Amount)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Member_register_dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.TE_CID = QTextEdit(Member_register_dialog)
        self.TE_CID.setObjectName(u"TE_CID")

        self.horizontalLayout_4.addWidget(self.TE_CID)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Member_register_dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.TE_SID = QTextEdit(Member_register_dialog)
        self.TE_SID.setObjectName(u"TE_SID")

        self.horizontalLayout_5.addWidget(self.TE_SID)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(Member_register_dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_9 = QLabel(Member_register_dialog)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_5 = QLabel(Member_register_dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Member_register_dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(Member_register_dialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.line_2 = QFrame(Member_register_dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.btn_MakeMember = QDialogButtonBox(Member_register_dialog)
        self.btn_MakeMember.setObjectName(u"btn_MakeMember")
        self.btn_MakeMember.setOrientation(Qt.Horizontal)
        self.btn_MakeMember.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.btn_MakeMember)


        self.retranslateUi(Member_register_dialog)
        self.btn_MakeMember.accepted.connect(Member_register_dialog.accept)
        self.btn_MakeMember.rejected.connect(Member_register_dialog.reject)

        QMetaObject.connectSlotsByName(Member_register_dialog)
    # setupUi

    def retranslateUi(self, Member_register_dialog):
        Member_register_dialog.setWindowTitle(QCoreApplication.translate("Member_register_dialog", u"\uba85\ub2e8 \uc0dd\uc131\uae30", None))
        self.label.setText(QCoreApplication.translate("Member_register_dialog", u"\uae30\uc218", None))
        self.label_2.setText(QCoreApplication.translate("Member_register_dialog", u"\ud6c4\ubcf4\uc0dd \uc778\uc6d0", None))
        self.label_4.setText(QCoreApplication.translate("Member_register_dialog", u"\ucd5c\uc120\ubc88 \ub2e8\ubc88(\uc804\uc0b0)", None))
        self.TE_CID.setHtml(QCoreApplication.translate("Member_register_dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Member_register_dialog", u"\ucd5c\uc120\ubc88 \ub2e8\ubc88(\uad50\ub0b4)", None))
        self.TE_SID.setHtml(QCoreApplication.translate("Member_register_dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">101</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Member_register_dialog", u"*\ubaa8\ub4e0 \uce78\uc5d0\ub294 \uc22b\uc790\ub9cc \uc785\ub825\ud574 \uc8fc\uc138\uc694*", None))
        self.label_5.setText(QCoreApplication.translate("Member_register_dialog", u"\ub2e8\ubc88(\uc804\uc0b0)\uc740 62-xxxx-yyy \uc5d0\uc11c\uc758 'yyy', \ub2e8\ubc88(\uad50\ub0b4\ub294) \uad50\ub0b4\uc5d0\uc11c \uc0ac\uc6a9\ud558\ub294 \uc138\uc790\ub9ac \ub2e8\ubc88\uc744 \uae30\uc785\ud558\uc2dc\uba74 \ub429\ub2c8\ub2e4.", None))
        self.label_6.setText(QCoreApplication.translate("Member_register_dialog", u"\uc131\ubcc4\uc5d0\ub294 \ub0a8\ud6c4\ubcf4\uc0dd\uc740 'M', \uc5ec\ud6c4\ubcf4\uc0dd\uc740 'F'\ub85c \uae30\uc785\ud574\uc8fc\uc2dc\uba74 \ub429\ub2c8\ub2e4.", None))
        self.label_7.setText(QCoreApplication.translate("Member_register_dialog", u"\uc131\ubcc4 \uc815\ubcf4\ub294 \ub0a8\ub140 \uccb4\ub825 \uae30\uc900\uc774 \ub2ec\ub77c\uc11c \uc81c\ub300\ub85c \ubc18\uc601\ud558\uae30 \uc704\ud574 \uc815\ud655\ud788 \uae30\uc785\ud574\uc8fc\uc154\uc57c \ud569\ub2c8\ub2e4", None))
    # retranslateUi

