# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(600, 600)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        Form.setMaximumSize(QtCore.QSize(600, 600))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 421, 541))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.widget)
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 4, 0, 1, 5)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 5, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 3, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 2, 0, 1, 6)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 3, 1, 3)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox.setEditable(False)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 4, 1, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_3.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 4, 8, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_3.addWidget(self.lineEdit_9, 1, 2, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 4, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_3.addWidget(self.lineEdit_10, 1, 7, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setAcceptDrops(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 3, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 5, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 8, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.widget)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 5, 0, 1, 9)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_3.addWidget(self.lineEdit_14, 4, 6, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 4, 3, 1, 3)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_3.addWidget(self.lineEdit_12, 2, 6, 1, 2)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_3.addWidget(self.lineEdit_13, 3, 6, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 9)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 2)
        self.gridLayout_3.setColumnStretch(5, 2)
        self.gridLayout_3.setColumnStretch(6, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 5, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 5, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 2, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_4.addWidget(self.lineEdit_19, 3, 6, 1, 2)
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 2, 5, 1, 2)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 4, 3, 1, 3)
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 5, 8, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 2, 4, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 2, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 2, 8, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.widget)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 5, 3, 1, 3)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_4.addWidget(self.lineEdit_20, 4, 6, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setAcceptDrops(False)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 3, 3, 1, 3)
        self.label_35 = QtWidgets.QLabel(self.widget)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 9)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 2, 2, 1, 2)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 2, 7, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.widget)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 6, 0, 1, 9)
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_4.addWidget(self.lineEdit_18, 5, 6, 1, 2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 3, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 1, 0, 1, 9)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 2)
        self.gridLayout_4.setColumnStretch(5, 2)
        self.gridLayout_4.setColumnStretch(6, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_5.addWidget(self.lineEdit_21, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.widget)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "道路类型"))
        self.label_5.setText(_translate("Form", "道路限速"))
        self.label_3.setText(_translate("Form", "车道数量"))
        self.lineEdit.setPlaceholderText(_translate("Form", "TestRun Name"))
        self.pushButton.setText(_translate("Form", "上传TestRun"))
        self.label.setText(_translate("Form", "TestRun 基本信息"))
        self.label_2.setText(_translate("Form", "车道长度"))
        self.label_7.setText(_translate("Form", "小客车"))
        self.label_8.setText(_translate("Form", "小货车"))
        self.label_6.setText(_translate("Form", "交通流车型"))
        self.label_9.setText(_translate("Form", "大货车"))
        self.label_17.setText(_translate("Form", "n/km"))
        self.label_19.setText(_translate("Form", "交通目标数量"))
        self.label_14.setText(_translate("Form", "m"))
        self.comboBox.setItemText(0, _translate("Form", "激进"))
        self.comboBox.setItemText(1, _translate("Form", "普通"))
        self.comboBox.setItemText(2, _translate("Form", "保守"))
        self.label_16.setText(_translate("Form", "交通流密度"))
        self.label_22.setText(_translate("Form", "km/h"))
        self.label_20.setText(_translate("Form", "交通流种类"))
        self.label_18.setText(_translate("Form", "交通流状态"))
        self.label_12.setText(_translate("Form", "起点"))
        self.label_13.setText(_translate("Form", "终点"))
        self.label_15.setText(_translate("Form", "m"))
        self.label_11.setText(_translate("Form", "交通流范围"))
        self.label_21.setText(_translate("Form", "交通流速度"))
        self.label_10.setText(_translate("Form", "设置交通流"))
        self.label_28.setText(_translate("Form", "交通流种类"))
        self.label_33.setText(_translate("Form", "交通流范围"))
        self.label_31.setText(_translate("Form", "终点"))
        self.label_24.setText(_translate("Form", "交通目标数量"))
        self.label_27.setText(_translate("Form", "km/h"))
        self.label_25.setText(_translate("Form", "m"))
        self.label_30.setText(_translate("Form", "起点"))
        self.label_32.setText(_translate("Form", "m"))
        self.label_34.setText(_translate("Form", "交通流速度"))
        self.label_29.setText(_translate("Form", "交通流状态"))
        self.label_35.setText(_translate("Form", "设置混合流"))
        self.label_26.setText(_translate("Form", "交通流密度"))
        self.label_23.setText(_translate("Form", "n/km"))
        self.checkBox.setText(_translate("Form", "是否为混合流"))
        self.pushButton_2.setText(_translate("Form", "生成"))
        self.lineEdit_21.setPlaceholderText(_translate("Form", "NewTestRun Name"))
        self.pushButton_3.setText(_translate("Form", "下载"))
        self.label_36.setText(_translate("Form", "生成TestRun"))
