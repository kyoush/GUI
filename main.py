#-*- coding: utf-8 -*-

# ---- PyQt5 ---- must to be installed

import sys
import datetime,time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

an = [40000, 39000, 38000, 37000, 36000, 35000, 34000, 33333, 33000, 32000, 31000,  30000, 29000, 28000, 27000, 26000, 25000, 24000, 23000, 22222, 22000, 21000, 20000, 15000, 12345, 11111, 10000, 5000, 1000, 100, 10, 0, 0]

def aniv(year, month, day):
    today = datetime.date.today()

    for i in range(1, 33):
    
        birthday = datetime.date(year, month , day)
        life = today - birthday

        if int(life.days) < 0 :
            return 'あなたはまだ生まれていません!'
            break
        elif birthday.month == today.month and birthday.day == today.day:

            if int(life.days) == an[i]:
                return 'お誕生日おめでとうございます!!\nおめでとうございます!\n今日はなんとあなたが生まれてから' +str(life.days)+ '日記念日です!'
                break
            elif int(life.days) + 1 == an[i]:
                return 'お誕生日おめでとうございます!!\n明日,あなたは生まれてから' +str(an[i])+ '日記念日を迎えます!\n今から急いでケーキを買いにに行こう!'
                break
            elif int(life.days) + 2 == an[i]:
                return 'お誕生日おめでとうございます!!\nあさって,あなたは生まれてから' +str(an[i])+ '日記念日を迎えます!今日気付いてよかったね!'
                break
            elif int(life.days) > an[i]:
                anver = an[i-1]
                remain = anver - int(life.days)
                anv = today + datetime.timedelta(days=remain)
                return 'お誕生日おめでとうございます!!\n今日はあなたが生まれてから' +str(life.days)+ '日記念日です!\nちなみに,あなたは'+anv.strftime("%Y")+'年の'+anv.strftime("%m")+'月'+anv.strftime("%d")+'日に'+str(anver)+'日記念日を迎えます!'
                break
        else:
            if int(life.days) == an[i]:
                return 'おめでとうございます!\n今日はなんとあなたが生まれてから' +str(life.days)+ '日記念日です!'
                break
            elif int(life.days) + 1 == an[i]:
                return '\n明日,あなたは生まれてから' +str(an[i])+ '日記念日を迎えます!\n今から急いでケーキを買いに行こう!'
                break
            elif int(life.days) + 2 == an[i]:
                return '\nあさって,あなたは生まれてから' +str(an[i])+ '日記念日を迎えます!\n今日気付いてよかったね!'
                break
            elif int(life.days) > an[i]:
                anver = an[i-1]
                remain = anver - int(life.days)
                anv = today + datetime.timedelta(days=remain)
                return '\n今日はあなたが生まれてから' +str(life.days)+ '日記念日です!\nちなみに,あなたは'+anv.strftime("%Y")+'年の'+anv.strftime("%m")+'月'+anv.strftime("%d")+'日に'+str(anver)+'日記念日を迎えます!'
                break

class Main(QWidget):

    def __init__(self):
        super().__init__()

        #ラベル
        self.title = QLabel('あなたの誕生日を入力して下さい')
        self.year = QLabel('何年?')
        self.month = QLabel('何月?')
        self.day = QLabel('何日?')
        self.y = QLabel('年(西暦)')
        self.m = QLabel('月')
        self.d = QLabel('日')

        self.yearEdit = QLineEdit()
        self.monthEdit = QLineEdit()
        self.dayEdit = QLineEdit()

        self.btn = QPushButton("結果は...?", self)
        self.cancel = QPushButton("クリア", self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.title, 1, 1)
        grid.addWidget(self.year, 2, 0)
        grid.addWidget(self.yearEdit, 2, 1)
        grid.addWidget(self.y, 2, 2)
        grid.addWidget(self.month, 3, 0)
        grid.addWidget(self.monthEdit, 3, 1)
        grid.addWidget(self.m, 3, 2)
        grid.addWidget(self.day, 4, 0)
        grid.addWidget(self.dayEdit, 4, 1)
        grid.addWidget(self.d, 4, 2)
        grid.addWidget(self.btn, 5, 1)
        grid.addWidget(self.cancel, 5, 0)

        self.setLayout(grid)

        self.resize(400, 250)
        self.center()
        self.setWindowTitle('記念日祝福プログラム')

        self.btn.clicked.connect(self.makeWindow)
        self.cancel.clicked.connect(self.yearEdit.clear)
        self.cancel.clicked.connect(self.monthEdit.clear)
        self.cancel.clicked.connect(self.dayEdit.clear)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.makeWindow()
            
    def makeWindow(self):
        if self.yearEdit.text() == '' or self.monthEdit.text() == '' or self.dayEdit.text() == '':
            str = '値を入力してください'
        else:
            inyear = int(self.yearEdit.text())
            inmonth = int(self.monthEdit.text())
            inday = int(self.dayEdit.text())
            str = aniv(inyear, inmonth, inday)
        
        subWindow = SubWindow(str)

        subWindow.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



class SubWindow(QWidget):

    def __init__(self, str, parent=None):
        self.w = QDialog(parent)
        label = QLabel(str)
        layout = QHBoxLayout()
        layout.addWidget(label)
        self.w.setLayout(layout)

    def show(self):
        self.w.exec_()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()

    main.show()
    sys.exit(app.exec_())
