import sys, os
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import QDir, QAbstractTableModel

#-- Ui import --#
from UI.ui_Main import Ui_MainWindow  # UI 파일에서 생성한 클래스 import
from UI.ui_App_info import *
from UI.ui_Edit_Members import *
from UI.ui_Edit_Record_dialog import *
from UI.ui_MemberList_Maker_dialog import *
from UI.ui_Settings import *

#-- moudules --#
import pandas as pd
import openpyxl

#-- etc --#
import qdarktheme


# -- 본문 -- #
selected_Path_Member = ''


#-- 다이얼로그 클래스 선언 --#
class AppInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AppInfo_dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("프로그램 정보")

class MemberList_Maker_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Member_register_dialog()
        self.ui.setupUi(self)

        self.ui.btn_MakeMember.clicked.connect(self.makeMemberfile)

    def makeMemberfile(self):
        grade = int(self.ui.TE_Grade.toPlainText())
        amount = int(self.ui.TE_Amount.toPlainText())
        cid = int(self.ui.TE_CID.toPlainText())
        sid = int(self.ui.TE_SID.toPlainText())

        print(grade, amount, cid, sid)

        df = pd.DataFrame( {
            '기수':[] ,
            '단번(교내)': [],
            '단번(전산)': [],
            '이름':[] ,
            '성별(M/F)': [],
            '전화번호': [],

        })

        for i in range(0, amount):
            df.loc[i, '기수'] = grade
            df.loc[i, '단번(전산)'] = cid + i
            df.loc[i, '단번(교내)'] = sid + i

        export_exelName = 'Members/' + str(grade) + '기 명단.xlsx'

        df.to_excel(export_exelName, index = False, header=True)



class EditMembers_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_EditMembers_dialog()
        self.ui.setupUi(self)

        global selected_Path_Member
        df = pd.read_excel(selected_Path_Member, header = 0)
        print(df)

        # 표의 크기를 설정한다
        self.ui.tableWidget.setRowCount(len(df.index))
        self.ui.tableWidget.setColumnCount(len(df.columns))

        # for 루프를 사용하여 각 셀에 데이터를 채운다
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.tableWidget.setItem(i, j, item)

        self.ui.btn_save.clicked.connect(self.save_Changes)
        

    def save_Changes(self):
        global selected_Path_Member

        rowCount = self.ui.tableWidget.rowCount()
        columnCount = self.ui.tableWidget.columnCount()

        # add this line
        data = []

        for row in range(rowCount):
            rowData = []
            for column in range(columnCount):
                widgetItem = self.ui.tableWidget.item(row, column)
                if widgetItem and widgetItem.text:
                    rowData.append(widgetItem.text())
                else:
                    rowData.append('NULL')
            print(rowData)

            # add this line
            data.append(rowData)


        # change these two lines
        df = pd.DataFrame(data)
        df.columns = ['기수', '단번(교내)', '단번(전산)', '이름', '성별(M/F)', '전화번호']
        df.to_excel(selected_Path_Member, header=True, index=False)

        

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Settings_dialog()
        self.ui.setupUi(self)



class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        # UI 파일에서 생성한 클래스를 로드
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #-- 미구현 버튼 비활성화 --#
        self.ui.btn_Inbody.setEnabled(False)
        self.ui.btn_SquadManage.setEnabled(False)
        self.ui.btn_PictureManage.setEnabled(False)

        # 기본 페이지는 명단관리
        self.ui.stackedWidget.setCurrentIndex(0)  
        self.refresh_Memberlist()


        #-- 다이얼로그 연결 --#
        self.ui.actionView_AppInfo.triggered.connect(self.showAppInfoDialog)
        self.ui.btn_NewMember.clicked.connect(self.showMemberlistMakerDialog)
        self.ui.btn_setting.clicked.connect(self.showSettingsDialog)
        self.ui.btn_EditMember.clicked.connect(self.showEditMembersDialog)

        #-- Stack 연결 --#
        self.ui.btn_MemberManage.clicked.connect(self.MemberManagePage)
        self.ui.btn_TrainingManage.clicked.connect(self.TraingPage)
        self.ui.btn_RecordManage.clicked.connect(self.RecordPage)

        #-- 기능함수 연결 --#
        self.ui.list_Memberlist.itemClicked.connect(self.clicked_list_Memberlist_item)


       
    #-- 다이얼로그 함수 --#
    def showAppInfoDialog(self):
        dialog = AppInfoDialog(self)
        dialog.exec()

    def showMemberlistMakerDialog(self):
        dialog = MemberList_Maker_dialog(self)
        dialog.exec()
        self.refresh_Memberlist()

    def showEditMembersDialog(self):
        dialog = EditMembers_dialog(self)
        dialog.exec()
        self.refresh_Memberlist()

    def showSettingsDialog(self):
        dialog = SettingsDialog(self)
        dialog.exec()



    #-- 스택 전환 함수 --#
    def MemberManagePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def TraingPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.preview_training()

    def RecordPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)



    #-- 리스트 위젯 리프레시 함수 --#
    def refresh_Memberlist(self):
        self.ui.list_Memberlist.clear()
        files = []
        for file_name in os.listdir("Members"):
            if file_name.endswith(".xlsx"):
                files.append(file_name)

        self.ui.list_Memberlist.addItems(files)



    # 명단관리 리스트 위젯에서 클릭된 파일 경로
    def clicked_list_Memberlist_item(self):
        global selected_Path_Member
        selected_item = 'Members/' + self.ui.list_Memberlist.currentItem().text()
        selected_Path_Member = selected_item
        print(selected_Path_Member)



    def preview_training(self):
        # 파일 경로
        file_path = "Members/62기 명단_병합테스트.xlsx"

        # pandas로 엑셀 파일 읽기
        df = pd.read_excel(file_path)

        # QTableView에 표시하기 위해 모델 생성
        model = pandasModel(df)

        # 표시할 테이블뷰 설정
        self.ui.Preview_Training.setModel(model)
        self.ui.Preview_Training.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Preview_Training.setEditTriggers(QAbstractItemView.NoEditTriggers)


# pandasModel 클래스 정의
class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            try:
                return self._data.columns.tolist()[section]
            except (IndexError, ):
                return "not found"
        return None
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    qdarktheme.setup_theme("dark")
    main_window.show()
    sys.exit(app.exec())
