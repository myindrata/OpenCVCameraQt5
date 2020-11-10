# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(803, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setMinimumSize(QtCore.QSize(640, 480))
        self.image_label.setMaximumSize(QtCore.QSize(1280, 960))
        self.image_label.setText("")
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.capture_bt = QtWidgets.QPushButton(Form)
        self.capture_bt.setObjectName("capture_bt")
        self.verticalLayout.addWidget(self.capture_bt)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calib_bt = QtWidgets.QPushButton(Form)
        self.calib_bt.setObjectName("calib_bt")
        self.horizontalLayout.addWidget(self.calib_bt)
        self.text_Timg = QtWidgets.QTextEdit(Form)
        self.text_Timg.setMaximumSize(QtCore.QSize(200, 30))
        self.text_Timg.setDocumentTitle("")
        self.text_Timg.setObjectName("text_Timg")
        self.horizontalLayout.addWidget(self.text_Timg)
        self.text_Treal = QtWidgets.QTextEdit(Form)
        self.text_Treal.setMaximumSize(QtCore.QSize(200, 30))
        self.text_Treal.setObjectName("text_Treal")
        self.horizontalLayout.addWidget(self.text_Treal)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.capture_bt.setText(_translate("Form", "Capture"))
        self.calib_bt.setText(_translate("Form", "Calib"))
        self.text_Timg.setPlaceholderText(_translate("Form", "tinggi"))
        self.text_Treal.setPlaceholderText(_translate("Form", "real"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())