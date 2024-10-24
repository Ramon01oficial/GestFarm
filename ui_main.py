# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1074, 736)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_16 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_cliente = QPushButton(self.frame)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_cliente)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_relatorio = QPushButton(self.frame)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setStyleSheet(u"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_relatorio)


        self.verticalLayout_16.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ok = QTabWidget(self.pg_table)
        self.ok.setObjectName(u"ok")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.tw_estoque = QTableWidget(self.tables)
        if (self.tw_estoque.columnCount() < 5):
            self.tw_estoque.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tw_estoque.setObjectName(u"tw_estoque")
        font = QFont()
        font.setPointSize(12)
        self.tw_estoque.setFont(font)

        self.verticalLayout_6.addWidget(self.tw_estoque)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTableWidget(self.tables)
        if (self.tw_saida.columnCount() < 8):
            self.tw_saida.setColumnCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_saida.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setFont(font)

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_pdf = QPushButton(self.frame_2)
        self.btn_pdf.setObjectName(u"btn_pdf")
        self.btn_pdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pdf.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_pdf)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_excluir)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.ok.addTab(self.tables, "")

        self.verticalLayout_8.addWidget(self.ok)

        self.Pages.addWidget(self.pg_table)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_15 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_3 = QFrame(self.pg_contato)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(251, 255, 199);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 221, 61))
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 190, 211, 41))
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 360, 201, 51))
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 70, 31, 21))
        self.label_29.setPixmap(QPixmap(u"../../Imagens/OIP (2).jpeg"))
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 110, 41, 21))
        self.label_30.setPixmap(QPixmap(u"../../Imagens/OIP.jpeg"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 150, 41, 21))
        self.label_31.setPixmap(QPixmap(u"../../Imagens/OIP (1).jpeg"))
        self.label_31.setScaledContents(True)
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(60, 240, 281, 16))
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(60, 280, 291, 21))
        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(60, 330, 251, 21))
        self.label_40 = QLabel(self.frame_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(60, 420, 301, 21))
        self.label_41 = QLabel(self.frame_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(60, 530, 131, 21))
        self.label_42 = QLabel(self.frame_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(60, 470, 291, 21))
        self.label_43 = QLabel(self.frame_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(60, 70, 191, 21))
        self.label_44 = QLabel(self.frame_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(70, 110, 191, 21))
        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(70, 150, 201, 16))
        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 240, 41, 21))
        self.label_46.setPixmap(QPixmap(u"../../Imagens/OIP (2).jpeg"))
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 280, 41, 21))
        self.label_47.setPixmap(QPixmap(u"../../Imagens/OIP.jpeg"))
        self.label_47.setScaledContents(True)
        self.label_47.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 330, 41, 21))
        self.label_48.setPixmap(QPixmap(u"../../Imagens/OIP (1).jpeg"))
        self.label_48.setScaledContents(True)
        self.label_49 = QLabel(self.frame_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 420, 41, 21))
        self.label_49.setPixmap(QPixmap(u"../../Imagens/OIP (2).jpeg"))
        self.label_49.setScaledContents(True)
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_50 = QLabel(self.frame_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 470, 41, 21))
        self.label_50.setPixmap(QPixmap(u"../../Imagens/OIP.jpeg"))
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_51 = QLabel(self.frame_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 530, 41, 21))
        self.label_51.setPixmap(QPixmap(u"../../Imagens/OIP (1).jpeg"))
        self.label_51.setScaledContents(True)
        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(960, 580, 51, 41))
        self.label_52.setPixmap(QPixmap(u"../../Imagens/channels4_profile.jpg"))
        self.label_52.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_contato)
        self.pg_vendas = QWidget()
        self.pg_vendas.setObjectName(u"pg_vendas")
        self.verticalLayout_12 = QVBoxLayout(self.pg_vendas)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_24 = QLabel(self.pg_vendas)
        self.label_24.setObjectName(u"label_24")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_24.setFont(font1)
        self.label_24.setLayoutDirection(Qt.LeftToRight)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_24)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_34 = QLabel(self.pg_vendas)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_19.addWidget(self.label_34)

        self.txt_codprod = QLineEdit(self.pg_vendas)
        self.txt_codprod.setObjectName(u"txt_codprod")

        self.horizontalLayout_19.addWidget(self.txt_codprod)


        self.verticalLayout_12.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.pg_vendas)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_22.addWidget(self.label_36)

        self.txt_quantidade_2 = QLineEdit(self.pg_vendas)
        self.txt_quantidade_2.setObjectName(u"txt_quantidade_2")

        self.horizontalLayout_22.addWidget(self.txt_quantidade_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_37 = QLabel(self.pg_vendas)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_21.addWidget(self.label_37)

        self.txt_codcliente = QLineEdit(self.pg_vendas)
        self.txt_codcliente.setObjectName(u"txt_codcliente")

        self.horizontalLayout_21.addWidget(self.txt_codcliente)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_38 = QLabel(self.pg_vendas)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_23.addWidget(self.label_38)

        self.btn_realizarvenda = QPushButton(self.pg_vendas)
        self.btn_realizarvenda.setObjectName(u"btn_realizarvenda")
        self.btn_realizarvenda.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_realizarvenda.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.btn_realizarvenda)

        self.label_35 = QLabel(self.pg_vendas)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_23.addWidget(self.label_35)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.Pages.addWidget(self.pg_vendas)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_16 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);")

        self.horizontalLayout_4.addWidget(self.label)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_cadastro_usuario = QPushButton(self.pg_home)
        self.btn_cadastro_usuario.setObjectName(u"btn_cadastro_usuario")
        self.btn_cadastro_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro_usuario.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_cadastro_usuario)

        self.btn_cadastro_produto = QPushButton(self.pg_home)
        self.btn_cadastro_produto.setObjectName(u"btn_cadastro_produto")
        self.btn_cadastro_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro_produto.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_cadastro_produto)

        self.btn_cadastro_cliente = QPushButton(self.pg_home)
        self.btn_cadastro_cliente.setObjectName(u"btn_cadastro_cliente")
        self.btn_cadastro_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro_cliente.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_cadastro_cliente)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_4)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro_cliente = QWidget()
        self.pg_cadastro_cliente.setObjectName(u"pg_cadastro_cliente")
        self.verticalLayout_11 = QVBoxLayout(self.pg_cadastro_cliente)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.pg_cadastro_cliente)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.pg_cadastro_cliente)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.txt_nome_cliente = QLineEdit(self.pg_cadastro_cliente)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")

        self.horizontalLayout_12.addWidget(self.txt_nome_cliente)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_26 = QLabel(self.pg_cadastro_cliente)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_13.addWidget(self.label_26)

        self.txt_cnpj = QLineEdit(self.pg_cadastro_cliente)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.horizontalLayout_13.addWidget(self.txt_cnpj)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.btn_cadastrar_cliente_no_banco = QPushButton(self.pg_cadastro_cliente)
        self.btn_cadastrar_cliente_no_banco.setObjectName(u"btn_cadastrar_cliente_no_banco")
        self.btn_cadastrar_cliente_no_banco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_cliente_no_banco.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.btn_cadastrar_cliente_no_banco)

        self.Pages.addWidget(self.pg_cadastro_cliente)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_17 = QLabel(self.pg_cadastro_usuario)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_17)

        self.label_6 = QLabel(self.pg_cadastro_usuario)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.pg_cadastro_usuario)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")

        self.horizontalLayout_8.addWidget(self.txt_nome_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_cadastro_usuario)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_cpf = QLineEdit(self.pg_cadastro_usuario)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.horizontalLayout_7.addWidget(self.txt_cpf)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.pg_cadastro_usuario)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.pg_cadastro_usuario)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.txt_senha2 = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.pg_cadastro_usuario)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.btn_cadastrar_usuario_no_banco = QPushButton(self.pg_cadastro_usuario)
        self.btn_cadastrar_usuario_no_banco.setObjectName(u"btn_cadastrar_usuario_no_banco")
        self.btn_cadastrar_usuario_no_banco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_usuario_no_banco.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.btn_cadastrar_usuario_no_banco)

        self.label_18 = QLabel(self.pg_cadastro_usuario)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_14.addWidget(self.label_18)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_prox_venc = QWidget()
        self.pg_prox_venc.setObjectName(u"pg_prox_venc")
        self.verticalLayout = QVBoxLayout(self.pg_prox_venc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_27 = QLabel(self.pg_prox_venc)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_27)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_buscar = QPushButton(self.pg_prox_venc)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_buscar.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.btn_buscar)

        self.txt_buscar_produto = QLineEdit(self.pg_prox_venc)
        self.txt_buscar_produto.setObjectName(u"txt_buscar_produto")

        self.horizontalLayout_18.addWidget(self.txt_buscar_produto)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.tw_proximo_vencimento = QTableWidget(self.pg_prox_venc)
        if (self.tw_proximo_vencimento.columnCount() < 5):
            self.tw_proximo_vencimento.setColumnCount(5)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setText(u"C\u00f3digo");
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font4);
        self.tw_proximo_vencimento.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font4);
        self.tw_proximo_vencimento.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font4);
        self.tw_proximo_vencimento.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font4);
        self.tw_proximo_vencimento.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font4);
        self.tw_proximo_vencimento.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.tw_proximo_vencimento.setObjectName(u"tw_proximo_vencimento")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.tw_proximo_vencimento.setFont(font5)
        self.tw_proximo_vencimento.setLayoutDirection(Qt.LeftToRight)
        self.tw_proximo_vencimento.setStyleSheet(u"QHeaderView::section{\n"
"\n"
"	background-color: rgb(122, 122, 122);\n"
"\n"
"	\n"
"	font: 75 12pt \"Arial\";\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"QTableWidget{\n"
"	\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.tw_proximo_vencimento.setFrameShape(QFrame.NoFrame)
        self.tw_proximo_vencimento.setFrameShadow(QFrame.Sunken)
        self.tw_proximo_vencimento.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_proximo_vencimento.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tw_proximo_vencimento.setAutoScrollMargin(16)
        self.tw_proximo_vencimento.setDragEnabled(False)
        self.tw_proximo_vencimento.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tw_proximo_vencimento.setAlternatingRowColors(True)
        self.tw_proximo_vencimento.setShowGrid(True)
        self.tw_proximo_vencimento.setGridStyle(Qt.NoPen)
        self.tw_proximo_vencimento.setWordWrap(False)
        self.tw_proximo_vencimento.setCornerButtonEnabled(True)

        self.verticalLayout.addWidget(self.tw_proximo_vencimento)

        self.Pages.addWidget(self.pg_prox_venc)
        self.pg_cliente = QWidget()
        self.pg_cliente.setObjectName(u"pg_cliente")
        self.verticalLayout_14 = QVBoxLayout(self.pg_cliente)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.pg_cliente)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(False)
        self.label_4.setFont(font6)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.btn_buscar_cliente = QPushButton(self.pg_cliente)
        self.btn_buscar_cliente.setObjectName(u"btn_buscar_cliente")
        self.btn_buscar_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_buscar_cliente.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.btn_buscar_cliente)

        self.txt_buscar_cliente = QLineEdit(self.pg_cliente)
        self.txt_buscar_cliente.setObjectName(u"txt_buscar_cliente")

        self.horizontalLayout_20.addWidget(self.txt_buscar_cliente)


        self.verticalLayout_14.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tw_cliente = QTableWidget(self.pg_cliente)
        if (self.tw_cliente.columnCount() < 3):
            self.tw_cliente.setColumnCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setText(u"C\u00f3digo");
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font4);
        self.tw_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font4);
        self.tw_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font4);
        self.tw_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        self.tw_cliente.setObjectName(u"tw_cliente")
        self.tw_cliente.setFont(font5)
        self.tw_cliente.setLayoutDirection(Qt.LeftToRight)
        self.tw_cliente.setStyleSheet(u"QHeaderView::section{\n"
"\n"
"	background-color: rgb(122, 122, 122);\n"
"\n"
"	\n"
"	font: 75 12pt \"Arial\";\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"QTableWidget{\n"
"	\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.tw_cliente.setFrameShape(QFrame.NoFrame)
        self.tw_cliente.setFrameShadow(QFrame.Sunken)
        self.tw_cliente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_cliente.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tw_cliente.setAutoScrollMargin(16)
        self.tw_cliente.setDragEnabled(False)
        self.tw_cliente.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tw_cliente.setAlternatingRowColors(True)
        self.tw_cliente.setShowGrid(True)
        self.tw_cliente.setGridStyle(Qt.NoPen)
        self.tw_cliente.setWordWrap(False)
        self.tw_cliente.setCornerButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.tw_cliente)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_excluir_cliente = QPushButton(self.pg_cliente)
        self.btn_excluir_cliente.setObjectName(u"btn_excluir_cliente")
        self.btn_excluir_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir_cliente.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_excluir_cliente)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_24.addLayout(self.verticalLayout_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_24)

        self.Pages.addWidget(self.pg_cliente)
        self.pg_cadastro_produto = QWidget()
        self.pg_cadastro_produto.setObjectName(u"pg_cadastro_produto")
        self.verticalLayout_10 = QVBoxLayout(self.pg_cadastro_produto)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_22 = QLabel(self.pg_cadastro_produto)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_22)

        self.label_11 = QLabel(self.pg_cadastro_produto)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.pg_cadastro_produto)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.txt_nomeprod = QLineEdit(self.pg_cadastro_produto)
        self.txt_nomeprod.setObjectName(u"txt_nomeprod")

        self.horizontalLayout_11.addWidget(self.txt_nomeprod)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.pg_cadastro_produto)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.txt_quantidade = QLineEdit(self.pg_cadastro_produto)
        self.txt_quantidade.setObjectName(u"txt_quantidade")

        self.horizontalLayout_10.addWidget(self.txt_quantidade)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.pg_cadastro_produto)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.txt_validade = QLineEdit(self.pg_cadastro_produto)
        self.txt_validade.setObjectName(u"txt_validade")

        self.horizontalLayout_9.addWidget(self.txt_validade)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.pg_cadastro_produto)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.txt_preco = QLineEdit(self.pg_cadastro_produto)
        self.txt_preco.setObjectName(u"txt_preco")

        self.horizontalLayout_17.addWidget(self.txt_preco)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.pg_cadastro_produto)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_15.addWidget(self.label_20)

        self.btn_cadastro_produto_no_banco = QPushButton(self.pg_cadastro_produto)
        self.btn_cadastro_produto_no_banco.setObjectName(u"btn_cadastro_produto_no_banco")
        self.btn_cadastro_produto_no_banco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro_produto_no_banco.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.btn_cadastro_produto_no_banco)

        self.label_21 = QLabel(self.pg_cadastro_produto)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.Pages.addWidget(self.pg_cadastro_produto)

        self.verticalLayout_16.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)
        self.ok.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_cliente.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        ___qtablewidgetitem = self.tw_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo Produto", None));
        ___qtablewidgetitem1 = self.tw_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tw_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tw_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtablewidgetitem4 = self.tw_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        ___qtablewidgetitem5 = self.tw_saida.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo saida", None));
        ___qtablewidgetitem6 = self.tw_saida.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo produto", None));
        ___qtablewidgetitem7 = self.tw_saida.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome produto", None));
        ___qtablewidgetitem8 = self.tw_saida.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtablewidgetitem9 = self.tw_saida.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem10 = self.tw_saida.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo cliente", None));
        ___qtablewidgetitem11 = self.tw_saida.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nome Cliente", None));
        ___qtablewidgetitem12 = self.tw_saida.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Valor Total", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_pdf.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.ok.setTabText(self.ok.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Principal", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Ramon vitor </span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Pedro Manoel </span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Juan Victor</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">pedromanoelfreitas4@gmail.com</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">https://github.com/Pedro-Manoel-Freitas</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">@</span><span style=\" font-family:'gg sans,Noto Sans,Helvetica Neue,Helvetica,Arial,sans-serif,Apple Symbols'; font-size:16px; font-weight:600; color:#000000;\">pedro_.manoel</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">juanbritoleal@gmail.com</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">@_ juan  victor</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">https://github.com/JuanVictor18</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">vitorramon285@gmail.com</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Ramon01oficial</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">@ramon_vitorsz</span></p></body></html>", None))
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_48.setText("")
        self.label_49.setText("")
        self.label_50.setText("")
        self.label_51.setText("")
        self.label_52.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo Produto", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do cliente", None))
        self.label_38.setText("")
        self.btn_realizarvenda.setText(QCoreApplication.translate("MainWindow", u"Realizar Venda", None))
        self.label_35.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#0055ff;\">GestFarm</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#0055ff;\">Sistema de Gerenciamento</span></p></body></html>", None))
        self.btn_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA CADASTRO DE USU\u00c1RIO", None))
        self.btn_cadastro_produto.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA CADASTRO DE PRODUTO", None))
        self.btn_cadastro_cliente.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA CADASTRO DE CLIENTE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">CADASTRO DE CLIENTE</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nome Cliente", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CNPJ/CPF:", None))
        self.btn_cadastrar_cliente_no_banco.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#0055ff;\">CADASTRO DE USU\u00c1RIO</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cpf", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Confirma Senha:", None))
        self.label_19.setText("")
        self.btn_cadastrar_usuario_no_banco.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_18.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Produtos pr\u00f3ximos ao vencimento", None))
        self.btn_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.txt_buscar_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar produto", None))
        ___qtablewidgetitem13 = self.tw_proximo_vencimento.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem14 = self.tw_proximo_vencimento.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem15 = self.tw_proximo_vencimento.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtablewidgetitem16 = self.tw_proximo_vencimento.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.btn_buscar_cliente.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.txt_buscar_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar produto", None))
        ___qtablewidgetitem17 = self.tw_cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem18 = self.tw_cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        self.btn_excluir_cliente.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">CADASTRO PRODUTO</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Validade:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
        self.label_20.setText("")
        self.btn_cadastro_produto_no_banco.setText(QCoreApplication.translate("MainWindow", u"CADASTRO PRODUTO", None))
        self.label_21.setText("")
    # retranslateUi

