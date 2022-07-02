from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from klav import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.A.clicked.connect(self.A_pressed)
        self.ui.B.clicked.connect(self.B_pressed)
        self.ui.C.clicked.connect(self.C_pressed)
        self.ui.D.clicked.connect(self.D_pressed)
        self.ui.E.clicked.connect(self.E_pressed)
        self.ui.F.clicked.connect(self.F_pressed)
        self.ui.G.clicked.connect(self.G_pressed)
        self.ui.H.clicked.connect(self.H_pressed)
        self.ui.I.clicked.connect(self.I_pressed)
        self.ui.J.clicked.connect(self.J_pressed)
        self.ui.K.clicked.connect(self.K_pressed)
        self.ui.L.clicked.connect(self.L_pressed)
        self.ui.M.clicked.connect(self.M_pressed)
        self.ui.N.clicked.connect(self.N_pressed)
        self.ui.O.clicked.connect(self.O_pressed)
        self.ui.P.clicked.connect(self.P_pressed)
        self.ui.Q.clicked.connect(self.Q_pressed)
        self.ui.R.clicked.connect(self.R_pressed)
        self.ui.S.clicked.connect(self.S_pressed)
        self.ui.T.clicked.connect(self.T_pressed)
        self.ui.U.clicked.connect(self.U_pressed)
        self.ui.V.clicked.connect(self.V_pressed)
        self.ui.W.clicked.connect(self.W_pressed)
        self.ui.X.clicked.connect(self.X_pressed)
        self.ui.Y.clicked.connect(self.Y_pressed)
        self.ui.Z.clicked.connect(self.Z_pressed)
        self.ui.nuqta.clicked.connect(self.dotPressed)
        self.ui.verg.clicked.connect(self.comapPressed)
        self.ui.probel.clicked.connect(self.spacePressed)
        self.ui.backspace.clicked.connect(self.backspacePressed)
        self.ui.ENTER.clicked.connect(self.enterPressed)
        self.ui.pushButton_33.clicked.connect(self.capslockPressed)

    def A_pressed(self):
        self.btnpressed(self.ui.A.text())

    def B_pressed(self):
        self.btnpressed(self.ui.B.text())

    def C_pressed(self):
        self.btnpressed(self.ui.C.text())

    def D_pressed(self):
        self.btnpressed(self.ui.D.text())

    def E_pressed(self):
        self.btnpressed(self.ui.E.text())

    def F_pressed(self):
        self.btnpressed(self.ui.F.text())

    def G_pressed(self):
        self.btnpressed(self.ui.G.text())

    def H_pressed(self):
        self.btnpressed(self.ui.H.text())

    def I_pressed(self):
        self.btnpressed(self.ui.I.text())

    def J_pressed(self):
        self.btnpressed(self.ui.J.text())

    def K_pressed(self):
        self.btnpressed(self.ui.K.text())

    def L_pressed(self):
        self.btnpressed(self.ui.L.text())

    def M_pressed(self):
        self.btnpressed(self.ui.M.text())

    def N_pressed(self):
        self.btnpressed(self.ui.N.text())

    def O_pressed(self):
        self.btnpressed(self.ui.O.text())

    def P_pressed(self):
        self.btnpressed(self.ui.P.text())

    def Q_pressed(self):
        self.btnpressed(self.ui.Q.text())

    def R_pressed(self):
        self.btnpressed(self.ui.R.text())

    def S_pressed(self):
        self.btnpressed(self.ui.S.text())

    def T_pressed(self):
        self.btnpressed(self.ui.T.text())

    def U_pressed(self):
        self.btnpressed(self.ui.U.text())

    def V_pressed(self):
        self.btnpressed(self.ui.V.text())

    def W_pressed(self):
        self.btnpressed(self.ui.W.text())

    def X_pressed(self):
        self.btnpressed(self.ui.X.text())

    def Y_pressed(self):
        self.btnpressed(self.ui.Y.text())

    def Z_pressed(self):
        self.btnpressed(self.ui.Z.text())

    def dotPressed(self):
        self.btnpressed(self.ui.nuqta.text())

    def comapPressed(self):
        self.btnpressed(self.ui.verg.text())

    def spacePressed(self):
        self.btnpressed(" ")

    def backspacePressed(self):
        text = self.ui.lineEdit.text()
        if text != "":
            self.ui.lineEdit.setText(text[:len(text)-1])

    def enterPressed(self):
        text = self.ui.lineEdit.text()
        self.ui.listView.addItem(text)
        self.ui.lineEdit.setText("")

    def btnpressed(self, text):
        linetext = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(linetext + text)

    def capslockPressed(self):
        self.ui.A.setText(self.ui.A.text().swapcase())
        self.ui.B.setText(self.ui.B.text().swapcase())
        self.ui.C.setText(self.ui.C.text().swapcase())
        self.ui.D.setText(self.ui.D.text().swapcase())
        self.ui.E.setText(self.ui.E.text().swapcase())
        self.ui.F.setText(self.ui.F.text().swapcase())
        self.ui.G.setText(self.ui.G.text().swapcase())
        self.ui.H.setText(self.ui.H.text().swapcase())
        self.ui.I.setText(self.ui.I.text().swapcase())
        self.ui.J.setText(self.ui.J.text().swapcase())
        self.ui.K.setText(self.ui.K.text().swapcase())
        self.ui.L.setText(self.ui.L.text().swapcase())
        self.ui.M.setText(self.ui.M.text().swapcase())
        self.ui.N.setText(self.ui.N.text().swapcase())
        self.ui.O.setText(self.ui.O.text().swapcase())
        self.ui.P.setText(self.ui.P.text().swapcase())
        self.ui.Q.setText(self.ui.Q.text().swapcase())
        self.ui.R.setText(self.ui.R.text().swapcase())
        self.ui.S.setText(self.ui.S.text().swapcase())
        self.ui.T.setText(self.ui.T.text().swapcase())
        self.ui.U.setText(self.ui.U.text().swapcase())
        self.ui.V.setText(self.ui.V.text().swapcase())
        self.ui.W.setText(self.ui.W.text().swapcase())
        self.ui.X.setText(self.ui.X.text().swapcase())
        self.ui.Y.setText(self.ui.Y.text().swapcase())
        self.ui.Z.setText(self.ui.Z.text().swapcase())


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


