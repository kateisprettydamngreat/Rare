# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/utils/pathedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PathEdit(object):
    def setupUi(self, PathEdit):
        PathEdit.setObjectName("PathEdit")
        PathEdit.resize(385, 30)
        self.layout_pathedit = QtWidgets.QHBoxLayout(PathEdit)
        self.layout_pathedit.setContentsMargins(0, 0, 0, 0)
        self.layout_pathedit.setObjectName("layout_pathedit")
        self.text_edit = QtWidgets.QLineEdit(PathEdit)
        self.text_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.text_edit.setObjectName("text_edit")
        self.layout_pathedit.addWidget(self.text_edit)
        self.path_select = QtWidgets.QToolButton(PathEdit)
        self.path_select.setObjectName("path_select")
        self.layout_pathedit.addWidget(self.path_select)

        self.retranslateUi(PathEdit)
        QtCore.QMetaObject.connectSlotsByName(PathEdit)

    def retranslateUi(self, PathEdit):
        _translate = QtCore.QCoreApplication.translate
        PathEdit.setWindowTitle(_translate("PathEdit", "PathEdit"))
        self.text_edit.setPlaceholderText(_translate("PathEdit", "Default"))
        self.path_select.setText(_translate("PathEdit", "Browse..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PathEdit = QtWidgets.QWidget()
    ui = Ui_PathEdit()
    ui.setupUi(PathEdit)
    PathEdit.show()
    sys.exit(app.exec_())
