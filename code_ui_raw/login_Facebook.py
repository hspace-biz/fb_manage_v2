# Form implementation generated from reading ui file './ui_raw/login_Facebook.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login_Facebook(object):
    def setupUi(self, Login_Facebook):
        Login_Facebook.setObjectName("Login_Facebook")
        Login_Facebook.resize(452, 182)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Facebook.sizePolicy().hasHeightForWidth())
        Login_Facebook.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Login_Facebook)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(Login_Facebook)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_uid = QtWidgets.QLabel(Login_Facebook)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_uid.setFont(font)
        self.label_uid.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_uid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_uid.setObjectName("label_uid")
        self.verticalLayout.addWidget(self.label_uid)
        self.label_ip = QtWidgets.QLabel(Login_Facebook)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ip.setFont(font)
        self.label_ip.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_ip.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout.addWidget(self.label_ip)
        self.pushButton_login = QtWidgets.QPushButton(Login_Facebook)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)
        self.pushButton_update = QtWidgets.QPushButton(Login_Facebook)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.verticalLayout.addWidget(self.pushButton_update)

        self.retranslateUi(Login_Facebook)
        QtCore.QMetaObject.connectSlotsByName(Login_Facebook)

    def retranslateUi(self, Login_Facebook):
        _translate = QtCore.QCoreApplication.translate
        Login_Facebook.setWindowTitle(_translate("Login_Facebook", "Login"))
        self.label_name.setText(_translate("Login_Facebook", "Name"))
        self.label_uid.setText(_translate("Login_Facebook", "Uid"))
        self.label_ip.setText(_translate("Login_Facebook", "IP"))
        self.pushButton_login.setText(_translate("Login_Facebook", "Login"))
        self.pushButton_update.setText(_translate("Login_Facebook", "Update"))
