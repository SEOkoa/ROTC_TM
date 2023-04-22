# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_infodOOJhS.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AppInfo_dialog(object):
    def setupUi(self, AppInfo_dialog):
        if not AppInfo_dialog.objectName():
            AppInfo_dialog.setObjectName(u"AppInfo_dialog")
        AppInfo_dialog.resize(352, 191)
        self.gridLayout = QGridLayout(AppInfo_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Maker_layout = QVBoxLayout()
        self.Maker_layout.setSpacing(0)
        self.Maker_layout.setObjectName(u"Maker_layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(AppInfo_dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_3 = QLabel(AppInfo_dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.Maker_layout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.Maker_layout, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.Copyright_info = QHBoxLayout()
        self.Copyright_info.setObjectName(u"Copyright_info")
        self.label_5 = QLabel(AppInfo_dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)

        self.Copyright_info.addWidget(self.label_5)


        self.gridLayout.addLayout(self.Copyright_info, 6, 0, 1, 1)

        self.version_layout = QVBoxLayout()
        self.version_layout.setSpacing(0)
        self.version_layout.setObjectName(u"version_layout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Version_fixed = QLabel(AppInfo_dialog)
        self.Version_fixed.setObjectName(u"Version_fixed")

        self.horizontalLayout_3.addWidget(self.Version_fixed)

        self.Version_label = QLabel(AppInfo_dialog)
        self.Version_label.setObjectName(u"Version_label")

        self.horizontalLayout_3.addWidget(self.Version_label)


        self.version_layout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.version_layout, 1, 0, 1, 1)

        self.Link_layout = QHBoxLayout()
        self.Link_layout.setObjectName(u"Link_layout")
        self.Git_link = QLabel(AppInfo_dialog)
        self.Git_link.setObjectName(u"Git_link")
        self.Git_link.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.Link_layout.addWidget(self.Git_link)


        self.gridLayout.addLayout(self.Link_layout, 5, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(AppInfo_dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(AppInfo_dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)


        self.retranslateUi(AppInfo_dialog)

        QMetaObject.connectSlotsByName(AppInfo_dialog)
    # setupUi

    def retranslateUi(self, AppInfo_dialog):
        AppInfo_dialog.setWindowTitle(QCoreApplication.translate("AppInfo_dialog", u"\ud504\ub85c\uadf8\ub7a8 \uc815\ubcf4", None))
        self.label_4.setText(QCoreApplication.translate("AppInfo_dialog", u"\uc81c\uc791\uc790:", None))
        self.label_3.setText(QCoreApplication.translate("AppInfo_dialog", u"SEO.Koa", None))
        self.label_5.setText(QCoreApplication.translate("AppInfo_dialog", u"\u2696\ufe0f MIT Licence", None))
        self.Version_fixed.setText(QCoreApplication.translate("AppInfo_dialog", u"\ubc84\uc804:", None))
        self.Version_label.setText(QCoreApplication.translate("AppInfo_dialog", u"0.0.1V", None))
        self.Git_link.setText(QCoreApplication.translate("AppInfo_dialog", u"GitHub: github.com/SEOkoa", None))
        self.label_2.setText(QCoreApplication.translate("AppInfo_dialog", u"\uc81c\uc791\uc790 \uc804\uc5ed\uae4c\uc9c0", None))
        self.label.setText(QCoreApplication.translate("AppInfo_dialog", u" \uc77c", None))
    # retranslateUi

