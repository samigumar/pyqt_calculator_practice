import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_myCalculator(object):
    def setupUi(self, myCalculator):
        myCalculator.setObjectName("myCalculator")
        myCalculator.resize(437, 528)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(myCalculator)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainContainer = QtWidgets.QFrame(myCalculator)
        self.mainContainer.setStyleSheet("QFrame#mainContainer{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.mainContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.mainContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainContainer.setObjectName("mainContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display1 = QtWidgets.QFrame(self.mainContainer)
        self.display1.setMaximumSize(QtCore.QSize(16777215, 90))
        self.display1.setStyleSheet("QFrame#display1{\n"
"\n"
"    background-color: rgb(208, 208, 208);\n"
"}")
        self.display1.setFrameShape(QtWidgets.QFrame.Box)
        self.display1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display1.setObjectName("display1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.display1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_equation = QtWidgets.QLabel(self.display1)
        self.label_equation.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_equation.setStyleSheet("")
        self.label_equation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_equation.setText("")
        self.label_equation.setObjectName("label_equation")
        self.horizontalLayout_2.addWidget(self.label_equation)
        self.verticalLayout.addWidget(self.display1)
        self.display2 = QtWidgets.QFrame(self.mainContainer)
        self.display2.setMaximumSize(QtCore.QSize(16777215, 28))
        self.display2.setStyleSheet("QFrame#display2{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.display2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display2.setObjectName("display2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.display2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_mc = QtWidgets.QPushButton(self.display2)
        self.button_mc.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_mc.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_mc.setObjectName("button_mc")
        self.horizontalLayout.addWidget(self.button_mc)
        self.button_mr = QtWidgets.QPushButton(self.display2)
        self.button_mr.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_mr.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_mr.setObjectName("button_mr")
        self.horizontalLayout.addWidget(self.button_mr)
        self.button_mplus = QtWidgets.QPushButton(self.display2)
        self.button_mplus.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_mplus.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_mplus.setObjectName("button_mplus")
        self.horizontalLayout.addWidget(self.button_mplus)
        self.button_mminus = QtWidgets.QPushButton(self.display2)
        self.button_mminus.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_mminus.setStyleSheet("QPushButton#pushButton_4{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_mminus.setObjectName("button_mminus")
        self.horizontalLayout.addWidget(self.button_mminus)
        self.button_ms = QtWidgets.QPushButton(self.display2)
        self.button_ms.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_ms.setStyleSheet("QPushButton#pushButton_5{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_ms.setObjectName("button_ms")
        self.horizontalLayout.addWidget(self.button_ms)
        self.button_M = QtWidgets.QPushButton(self.display2)
        self.button_M.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_M.setStyleSheet("QPushButton#pushButton_6{\n"
"background-color: rgb(206, 206, 206);\n"
"font:9pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_M.setObjectName("button_M")
        self.horizontalLayout.addWidget(self.button_M)
        self.verticalLayout.addWidget(self.display2)
        self.keys = QtWidgets.QFrame(self.mainContainer)
        self.keys.setStyleSheet("")
        self.keys.setFrameShape(QtWidgets.QFrame.Box)
        self.keys.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keys.setObjectName("keys")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.keys)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.keycontainer1 = QtWidgets.QFrame(self.keys)
        self.keycontainer1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.keycontainer1.setStyleSheet("QFrame#keycontainer1{\n"
"background-color: rgb(243, 243, 243);\n"
"\n"
"}")
        self.keycontainer1.setFrameShape(QtWidgets.QFrame.Box)
        self.keycontainer1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keycontainer1.setLineWidth(0)
        self.keycontainer1.setObjectName("keycontainer1")
        self.gridLayout = QtWidgets.QGridLayout(self.keycontainer1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_3 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("3"))
        self.button_3.setMinimumSize(QtCore.QSize(60, 60))
        self.button_3.setMaximumSize(QtCore.QSize(300, 90))
        self.button_3.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 7, 3, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("0") )
        self.button_0.setMinimumSize(QtCore.QSize(60, 60))
        self.button_0.setMaximumSize(QtCore.QSize(300, 90))
        self.button_0.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 15, 2, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("+"))
        self.button_plus.setMinimumSize(QtCore.QSize(60, 60))
        self.button_plus.setMaximumSize(QtCore.QSize(300, 90))
        self.button_plus.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 7, 4, 1, 1)
        self.button_equal = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("="))
        self.button_equal.setMinimumSize(QtCore.QSize(60, 60))
        self.button_equal.setMaximumSize(QtCore.QSize(300, 90))
        self.button_equal.setStyleSheet("QPushButton#button_equal{\n"
"\n"
"background-color: rgb(148, 162, 200);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}")
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 15, 4, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("-"))
        self.button_minus.setMinimumSize(QtCore.QSize(60, 60))
        self.button_minus.setMaximumSize(QtCore.QSize(300, 90))
        self.button_minus.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 5, 4, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("2"))
        self.button_2.setMinimumSize(QtCore.QSize(60, 60))
        self.button_2.setMaximumSize(QtCore.QSize(300, 90))
        self.button_2.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 7, 2, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("5"))
        self.button_5.setMinimumSize(QtCore.QSize(60, 60))
        self.button_5.setMaximumSize(QtCore.QSize(300, 90))
        self.button_5.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 5, 2, 1, 1)
        self.button_negative = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("-"))
        self.button_negative.setMinimumSize(QtCore.QSize(60, 60))
        self.button_negative.setMaximumSize(QtCore.QSize(300, 90))
        self.button_negative.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_negative.setObjectName("button_negative")
        self.gridLayout.addWidget(self.button_negative, 15, 0, 1, 1)
        self.button_reciprocal = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("^"))
        self.button_reciprocal.setMinimumSize(QtCore.QSize(60, 60))
        self.button_reciprocal.setMaximumSize(QtCore.QSize(300, 90))
        self.button_reciprocal.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_reciprocal.setObjectName("button_reciprocal")
        self.gridLayout.addWidget(self.button_reciprocal, 1, 2, 1, 1)
        self.button_root = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("√"))
        self.button_root.setMinimumSize(QtCore.QSize(60, 60))
        self.button_root.setMaximumSize(QtCore.QSize(300, 90))
        self.button_root.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_root.setObjectName("button_root")
        self.gridLayout.addWidget(self.button_root, 1, 3, 1, 1)
        self.button_vulgar = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("/"))
        self.button_vulgar.setMinimumSize(QtCore.QSize(60, 60))
        self.button_vulgar.setMaximumSize(QtCore.QSize(300, 90))
        self.button_vulgar.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_vulgar.setObjectName("button_vulgar")
        self.gridLayout.addWidget(self.button_vulgar, 1, 0, 1, 1)
        self.button_division = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("/"))
        self.button_division.setMinimumSize(QtCore.QSize(60, 60))
        self.button_division.setMaximumSize(QtCore.QSize(300, 90))
        self.button_division.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_division.setObjectName("button_division")
        self.gridLayout.addWidget(self.button_division, 1, 4, 1, 1)
        self.button_dot = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("."))
        self.button_dot.setMinimumSize(QtCore.QSize(60, 60))
        self.button_dot.setMaximumSize(QtCore.QSize(300, 90))
        self.button_dot.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_dot.setObjectName("button_dot")
        self.gridLayout.addWidget(self.button_dot, 15, 3, 1, 1)
        self.button_clear_entry = QtWidgets.QPushButton(self.keycontainer1)
        self.button_clear_entry.setMinimumSize(QtCore.QSize(60, 60))
        self.button_clear_entry.setMaximumSize(QtCore.QSize(300, 90))
        self.button_clear_entry.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"\n"
"")
        self.button_clear_entry.setObjectName("button_clear_entry")
        self.gridLayout.addWidget(self.button_clear_entry, 0, 2, 1, 1)
        self.button_percent = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("%"))
        self.button_percent.setMinimumSize(QtCore.QSize(60, 60))
        self.button_percent.setMaximumSize(QtCore.QSize(300, 90))
        self.button_percent.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font:12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_percent.setObjectName("button_percent")
        self.gridLayout.addWidget(self.button_percent, 0, 0, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("C"))
        self.button_clear.setMinimumSize(QtCore.QSize(60, 60))
        self.button_clear.setMaximumSize(QtCore.QSize(300, 90))
        self.button_clear.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"\n"
"")
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 0, 3, 1, 1)
        self.button_backspace = QtWidgets.QPushButton(self.keycontainer1)
        self.button_backspace.setMinimumSize(QtCore.QSize(60, 60))
        self.button_backspace.setMaximumSize(QtCore.QSize(300, 90))
        self.button_backspace.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 8pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_backspace.setObjectName("button_backspace")
        self.gridLayout.addWidget(self.button_backspace, 0, 4, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("1"))
        self.button_1.setMinimumSize(QtCore.QSize(60, 60))
        self.button_1.setMaximumSize(QtCore.QSize(300, 90))
        self.button_1.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 7, 0, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("6"))
        self.button_6.setMinimumSize(QtCore.QSize(60, 60))
        self.button_6.setMaximumSize(QtCore.QSize(300, 90))
        self.button_6.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 5, 3, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("7"))
        self.button_7.setMinimumSize(QtCore.QSize(60, 60))
        self.button_7.setMaximumSize(QtCore.QSize(300, 90))
        self.button_7.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("8"))
        self.button_8.setMinimumSize(QtCore.QSize(60, 60))
        self.button_8.setMaximumSize(QtCore.QSize(300, 90))
        self.button_8.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 2, 2, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("9"))
        self.button_9.setMinimumSize(QtCore.QSize(60, 60))
        self.button_9.setMaximumSize(QtCore.QSize(300, 90))
        self.button_9.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 2, 3, 1, 1)
        self.button_product = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("*"))
        self.button_product.setMinimumSize(QtCore.QSize(60, 60))
        self.button_product.setMaximumSize(QtCore.QSize(300, 90))
        self.button_product.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border:1px solid rgb(206, 206, 206);\n"
"\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_product.setObjectName("button_product")
        self.gridLayout.addWidget(self.button_product, 2, 4, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.keycontainer1, clicked= lambda: self.press_it("4"))
        self.button_4.setMinimumSize(QtCore.QSize(60, 60))
        self.button_4.setMaximumSize(QtCore.QSize(300, 90))
        self.button_4.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(239, 239, 239);\n"
"border:1px solid rgb(206, 206, 206);\n"
"font: 75 12pt \"Arial\";\n"
"color:rgb(0, 0, 0)\n"
"\n"
"}\n"
"")
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 5, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.keycontainer1)
        self.verticalLayout.addWidget(self.keys)
        self.verticalLayout_2.addWidget(self.mainContainer)

        self.retranslateUi(myCalculator)
        QtCore.QMetaObject.connectSlotsByName(myCalculator)

    def press_it(self, pressed):
        if pressed == "C":
            self.label_equation.setText("0")
        else:
            if self.label_equation.text() == "0":
                self.label_equation.setText("")
            self.label_equation.setText(f'{self.label_equation.text()} {pressed}')

    def retranslateUi(self, myCalculator):
        _translate = QtCore.QCoreApplication.translate
        myCalculator.setWindowTitle(_translate("myCalculator", "Form"))
        self.button_mc.setText(_translate("myCalculator", "MC"))
        self.button_mr.setText(_translate("myCalculator", "MR"))
        self.button_mplus.setText(_translate("myCalculator", "M+"))
        self.button_mminus.setText(_translate("myCalculator", "M-"))
        self.button_ms.setText(_translate("myCalculator", "MS"))
        self.button_M.setText(_translate("myCalculator", "M"))
        self.button_3.setText(_translate("myCalculator", "3"))
        self.button_0.setText(_translate("myCalculator", "0"))
        self.button_plus.setText(_translate("myCalculator", "+"))
        self.button_equal.setText(_translate("myCalculator", "="))
        self.button_minus.setText(_translate("myCalculator", "-"))
        self.button_2.setText(_translate("myCalculator", "2"))
        self.button_5.setText(_translate("myCalculator", "5"))
        self.button_negative.setText(_translate("myCalculator", "+/-"))
        self.button_reciprocal.setText(_translate("myCalculator", "𝒙²"))
        self.button_root.setText(_translate("myCalculator", "√x"))
        self.button_vulgar.setText(_translate("myCalculator", "𝟏/𝒙 "))
        self.button_division.setText(_translate("myCalculator", "/"))
        self.button_dot.setText(_translate("myCalculator", "."))
        self.button_clear_entry.setText(_translate("myCalculator", "CE"))
        self.button_percent.setText(_translate("myCalculator", "%"))
        self.button_clear.setText(_translate("myCalculator", "C"))
        self.button_backspace.setText(_translate("myCalculator", "backspace"))
        self.button_1.setText(_translate("myCalculator", "1"))
        self.button_6.setText(_translate("myCalculator", "6"))
        self.button_7.setText(_translate("myCalculator", "7"))
        self.button_8.setText(_translate("myCalculator", "8"))
        self.button_9.setText(_translate("myCalculator", "9"))
        self.button_product.setText(_translate("myCalculator", "X"))
        self.button_4.setText(_translate("myCalculator", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myCalculator = QtWidgets.QWidget()
    ui = Ui_myCalculator()
    ui.setupUi(myCalculator)
    myCalculator.show()
    sys.exit(app.exec_())
