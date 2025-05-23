# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CollisionSimulator(object):
    def setupUi(self, CollisionSimulator):
        CollisionSimulator.setObjectName("CollisionSimulator")
        CollisionSimulator.resize(724, 652)
        CollisionSimulator.setMinimumSize(QtCore.QSize(724, 652))
        CollisionSimulator.setMaximumSize(QtCore.QSize(724, 652))
        CollisionSimulator.setSizeIncrement(QtCore.QSize(724, 652))
        CollisionSimulator.setBaseSize(QtCore.QSize(724, 652))
        self.object_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_label_1.setGeometry(QtCore.QRect(110, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.object_label_1.setFont(font)
        self.object_label_1.setObjectName("object_label_1")
        self.object_label_2 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_label_2.setGeometry(QtCore.QRect(350, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.object_label_2.setFont(font)
        self.object_label_2.setObjectName("object_label_2")
        self.graphicsView = QtWidgets.QGraphicsView(parent=CollisionSimulator)
        self.graphicsView.setGeometry(QtCore.QRect(11, 60, 700, 450))
        self.graphicsView.setMinimumSize(QtCore.QSize(700, 450))
        self.graphicsView.setMaximumSize(QtCore.QSize(700, 450))
        self.graphicsView.setSizeIncrement(QtCore.QSize(700, 450))
        self.graphicsView.setBaseSize(QtCore.QSize(700, 450))
        self.graphicsView.setObjectName("graphicsView")
        self.game_title_label = QtWidgets.QLabel(parent=CollisionSimulator)
        self.game_title_label.setGeometry(QtCore.QRect(110, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(18)
        self.game_title_label.setFont(font)
        self.game_title_label.setObjectName("game_title_label")
        self.error_message_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.error_message_label_1.setGeometry(QtCore.QRect(85, 625, 400, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_message_label_1.sizePolicy().hasHeightForWidth())
        self.error_message_label_1.setSizePolicy(sizePolicy)
        self.error_message_label_1.setMinimumSize(QtCore.QSize(400, 20))
        self.error_message_label_1.setMaximumSize(QtCore.QSize(400, 20))
        self.error_message_label_1.setSizeIncrement(QtCore.QSize(400, 20))
        self.error_message_label_1.setBaseSize(QtCore.QSize(400, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.error_message_label_1.setFont(font)
        self.error_message_label_1.setText("")
        self.error_message_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_message_label_1.setObjectName("error_message_label_1")
        self.mass__kg_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.mass__kg_label_1.setGeometry(QtCore.QRect(204, 593, 47, 23))
        self.mass__kg_label_1.setMinimumSize(QtCore.QSize(0, 23))
        self.mass__kg_label_1.setMaximumSize(QtCore.QSize(16777215, 23))
        self.mass__kg_label_1.setSizeIncrement(QtCore.QSize(0, 23))
        self.mass__kg_label_1.setBaseSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.mass__kg_label_1.setFont(font)
        self.mass__kg_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mass__kg_label_1.setObjectName("mass__kg_label_1")
        self.mass__kg_label_2 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.mass__kg_label_2.setGeometry(QtCore.QRect(444, 593, 47, 23))
        self.mass__kg_label_2.setMinimumSize(QtCore.QSize(0, 23))
        self.mass__kg_label_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.mass__kg_label_2.setSizeIncrement(QtCore.QSize(0, 23))
        self.mass__kg_label_2.setBaseSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.mass__kg_label_2.setFont(font)
        self.mass__kg_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mass__kg_label_2.setObjectName("mass__kg_label_2")
        self.velocity_ms_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.velocity_ms_label_1.setGeometry(QtCore.QRect(206, 560, 60, 23))
        self.velocity_ms_label_1.setMinimumSize(QtCore.QSize(0, 23))
        self.velocity_ms_label_1.setMaximumSize(QtCore.QSize(16777215, 23))
        self.velocity_ms_label_1.setSizeIncrement(QtCore.QSize(0, 23))
        self.velocity_ms_label_1.setBaseSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.velocity_ms_label_1.setFont(font)
        self.velocity_ms_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.velocity_ms_label_1.setObjectName("velocity_ms_label_1")
        self.velocity_ms_label_2 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.velocity_ms_label_2.setGeometry(QtCore.QRect(446, 560, 60, 23))
        self.velocity_ms_label_2.setMinimumSize(QtCore.QSize(0, 23))
        self.velocity_ms_label_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.velocity_ms_label_2.setSizeIncrement(QtCore.QSize(0, 23))
        self.velocity_ms_label_2.setBaseSize(QtCore.QSize(0, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.velocity_ms_label_2.setFont(font)
        self.velocity_ms_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.velocity_ms_label_2.setObjectName("velocity_ms_label_2")
        self.object_velocity_input_2 = QtWidgets.QLineEdit(parent=CollisionSimulator)
        self.object_velocity_input_2.setGeometry(QtCore.QRect(400, 560, 41, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_velocity_input_2.sizePolicy().hasHeightForWidth())
        self.object_velocity_input_2.setSizePolicy(sizePolicy)
        self.object_velocity_input_2.setMinimumSize(QtCore.QSize(41, 23))
        self.object_velocity_input_2.setMaximumSize(QtCore.QSize(41, 23))
        self.object_velocity_input_2.setSizeIncrement(QtCore.QSize(41, 23))
        self.object_velocity_input_2.setBaseSize(QtCore.QSize(41, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.object_velocity_input_2.setFont(font)
        self.object_velocity_input_2.setText("")
        self.object_velocity_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.object_velocity_input_2.setObjectName("object_velocity_input_2")
        self.object_mass_input_2 = QtWidgets.QLineEdit(parent=CollisionSimulator)
        self.object_mass_input_2.setGeometry(QtCore.QRect(400, 593, 41, 23))
        self.object_mass_input_2.setMinimumSize(QtCore.QSize(41, 23))
        self.object_mass_input_2.setMaximumSize(QtCore.QSize(41, 23))
        self.object_mass_input_2.setSizeIncrement(QtCore.QSize(41, 23))
        self.object_mass_input_2.setBaseSize(QtCore.QSize(41, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.object_mass_input_2.setFont(font)
        self.object_mass_input_2.setText("")
        self.object_mass_input_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.object_mass_input_2.setObjectName("object_mass_input_2")
        self.object_velocity_label_2 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_velocity_label_2.setGeometry(QtCore.QRect(310, 560, 77, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_velocity_label_2.sizePolicy().hasHeightForWidth())
        self.object_velocity_label_2.setSizePolicy(sizePolicy)
        self.object_velocity_label_2.setMinimumSize(QtCore.QSize(77, 23))
        self.object_velocity_label_2.setMaximumSize(QtCore.QSize(77, 23))
        self.object_velocity_label_2.setSizeIncrement(QtCore.QSize(77, 23))
        self.object_velocity_label_2.setBaseSize(QtCore.QSize(77, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.object_velocity_label_2.setFont(font)
        self.object_velocity_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.object_velocity_label_2.setObjectName("object_velocity_label_2")
        self.object_mass_label_2 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_mass_label_2.setGeometry(QtCore.QRect(310, 593, 77, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_mass_label_2.sizePolicy().hasHeightForWidth())
        self.object_mass_label_2.setSizePolicy(sizePolicy)
        self.object_mass_label_2.setMinimumSize(QtCore.QSize(77, 23))
        self.object_mass_label_2.setMaximumSize(QtCore.QSize(77, 23))
        self.object_mass_label_2.setSizeIncrement(QtCore.QSize(77, 23))
        self.object_mass_label_2.setBaseSize(QtCore.QSize(77, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.object_mass_label_2.setFont(font)
        self.object_mass_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.object_mass_label_2.setObjectName("object_mass_label_2")
        self.object_velocity_input_1 = QtWidgets.QLineEdit(parent=CollisionSimulator)
        self.object_velocity_input_1.setGeometry(QtCore.QRect(160, 560, 41, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_velocity_input_1.sizePolicy().hasHeightForWidth())
        self.object_velocity_input_1.setSizePolicy(sizePolicy)
        self.object_velocity_input_1.setMinimumSize(QtCore.QSize(41, 23))
        self.object_velocity_input_1.setMaximumSize(QtCore.QSize(41, 23))
        self.object_velocity_input_1.setSizeIncrement(QtCore.QSize(41, 23))
        self.object_velocity_input_1.setBaseSize(QtCore.QSize(41, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.object_velocity_input_1.setFont(font)
        self.object_velocity_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.object_velocity_input_1.setObjectName("object_velocity_input_1")
        self.object_mass_input_1 = QtWidgets.QLineEdit(parent=CollisionSimulator)
        self.object_mass_input_1.setGeometry(QtCore.QRect(160, 593, 41, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_mass_input_1.sizePolicy().hasHeightForWidth())
        self.object_mass_input_1.setSizePolicy(sizePolicy)
        self.object_mass_input_1.setMinimumSize(QtCore.QSize(41, 23))
        self.object_mass_input_1.setMaximumSize(QtCore.QSize(41, 23))
        self.object_mass_input_1.setSizeIncrement(QtCore.QSize(41, 23))
        self.object_mass_input_1.setBaseSize(QtCore.QSize(41, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.object_mass_input_1.setFont(font)
        self.object_mass_input_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.object_mass_input_1.setObjectName("object_mass_input_1")
        self.object_mass_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_mass_label_1.setGeometry(QtCore.QRect(70, 593, 77, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_mass_label_1.sizePolicy().hasHeightForWidth())
        self.object_mass_label_1.setSizePolicy(sizePolicy)
        self.object_mass_label_1.setMinimumSize(QtCore.QSize(77, 23))
        self.object_mass_label_1.setMaximumSize(QtCore.QSize(77, 23))
        self.object_mass_label_1.setSizeIncrement(QtCore.QSize(77, 23))
        self.object_mass_label_1.setBaseSize(QtCore.QSize(77, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.object_mass_label_1.setFont(font)
        self.object_mass_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.object_mass_label_1.setObjectName("object_mass_label_1")
        self.object_velocity_label_1 = QtWidgets.QLabel(parent=CollisionSimulator)
        self.object_velocity_label_1.setGeometry(QtCore.QRect(70, 560, 77, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_velocity_label_1.sizePolicy().hasHeightForWidth())
        self.object_velocity_label_1.setSizePolicy(sizePolicy)
        self.object_velocity_label_1.setMinimumSize(QtCore.QSize(77, 23))
        self.object_velocity_label_1.setMaximumSize(QtCore.QSize(77, 23))
        self.object_velocity_label_1.setSizeIncrement(QtCore.QSize(77, 23))
        self.object_velocity_label_1.setBaseSize(QtCore.QSize(77, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.object_velocity_label_1.setFont(font)
        self.object_velocity_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.object_velocity_label_1.setObjectName("object_velocity_label_1")
        self.start_pushButton = QtWidgets.QPushButton(parent=CollisionSimulator)
        self.start_pushButton.setGeometry(QtCore.QRect(550, 560, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setObjectName("start_pushButton")
        self.restart_pushButton = QtWidgets.QPushButton(parent=CollisionSimulator)
        self.restart_pushButton.setGeometry(QtCore.QRect(550, 593, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.restart_pushButton.setFont(font)
        self.restart_pushButton.setObjectName("restart_pushButton")

        self.retranslateUi(CollisionSimulator)
        QtCore.QMetaObject.connectSlotsByName(CollisionSimulator)

    def retranslateUi(self, CollisionSimulator):
        _translate = QtCore.QCoreApplication.translate
        CollisionSimulator.setWindowTitle(_translate("CollisionSimulator", "1D Collision Simulator Project"))
        self.object_label_1.setText(_translate("CollisionSimulator", "Object 1"))
        self.object_label_2.setText(_translate("CollisionSimulator", "Object 2"))
        self.game_title_label.setText(_translate("CollisionSimulator", "1D Collision Simulator"))
        self.mass__kg_label_1.setText(_translate("CollisionSimulator", "(kg)"))
        self.mass__kg_label_2.setText(_translate("CollisionSimulator", "(kg)"))
        self.velocity_ms_label_1.setText(_translate("CollisionSimulator", "(m/s)"))
        self.velocity_ms_label_2.setText(_translate("CollisionSimulator", "(m/s)"))
        self.object_velocity_label_2.setText(_translate("CollisionSimulator", "Velocity"))
        self.object_mass_label_2.setText(_translate("CollisionSimulator", "Mass"))
        self.object_mass_label_1.setText(_translate("CollisionSimulator", "Mass"))
        self.object_velocity_label_1.setText(_translate("CollisionSimulator", "Velocity"))
        self.start_pushButton.setText(_translate("CollisionSimulator", "START"))
        self.restart_pushButton.setText(_translate("CollisionSimulator", "RESTART"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CollisionSimulator = QtWidgets.QWidget()
    ui = Ui_CollisionSimulator()
    ui.setupUi(CollisionSimulator)
    CollisionSimulator.show()
    sys.exit(app.exec())
