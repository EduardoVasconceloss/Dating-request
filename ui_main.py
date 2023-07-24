# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainghknRa.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(462, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"  background-color: qlineargradient(\n"
"    spread: pad,\n"
"    x1: 0,\n"
"    y1: 0,\n"
"    x2: 1,\n"
"    y2: 0,\n"
"    stop: 0 rgba(255, 138, 173, 255),\n"
"    stop: 0.55 rgba(235, 169, 221, 255),\n"
"    stop: 0.98 rgba(214, 159, 195, 255),\n"
"    stop: 1 rgba(0, 0, 0, 0)\n"
"  );\n"
"}\n"
"\n"
"QLabel#querNamorarCmg {\n"
"  font-size: 35px;\n"
"  font-weight: bold;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"  border: 2px solid white;\n"
"  font_size: 20px;\n"
"  font-weight: bold;\n"
"  color: rgba(255, 138, 173, 255);\n"
"  min-height: 40px;\n"
"  border-radius: 20px;\n"
"  background-color: white;\n"
"}")
        self.querNamorarCmg = QLabel(self.centralwidget)
        self.querNamorarCmg.setObjectName(u"querNamorarCmg")
        self.querNamorarCmg.setGeometry(QRect(10, 9, 441, 61))
        self.querNamorarCmg.setAlignment(Qt.AlignCenter)
        self.frame_sim = QFrame(self.centralwidget)
        self.frame_sim.setObjectName(u"frame_sim")
        self.frame_sim.setGeometry(QRect(70, 170, 101, 61))
        self.frame_sim.setFrameShape(QFrame.NoFrame)
        self.frame_sim.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_sim)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.botao_sim = QPushButton(self.frame_sim)
        self.botao_sim.setObjectName(u"botao_sim")

        self.horizontalLayout.addWidget(self.botao_sim)

        self.frame_nao = QFrame(self.centralwidget)
        self.frame_nao.setObjectName(u"frame_nao")
        self.frame_nao.setGeometry(QRect(290, 170, 100, 61))
        self.frame_nao.setFrameShape(QFrame.NoFrame)
        self.frame_nao.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nao)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.botao_nao = QPushButton(self.frame_nao)
        self.botao_nao.setObjectName(u"botao_nao")

        self.horizontalLayout_2.addWidget(self.botao_nao)

        self.coracao = QLabel(self.centralwidget)
        self.coracao.setObjectName(u"coracao")
        self.coracao.setGeometry(QRect(80, 80, 301, 251))
        self.coracao.setPixmap(QPixmap(u":/assets/coracao.png"))
        self.coracao.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 462, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.querNamorarCmg.setText(QCoreApplication.translate("MainWindow", u"Quer namorar comigo?", None))
        self.botao_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.botao_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.coracao.setText("")
    # retranslateUi

