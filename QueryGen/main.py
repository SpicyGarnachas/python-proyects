from PyQt5 import uic, QtWidgets
import Name_Generator
import PassGen
import EmailGen
import random
import sys

qtCreatorFile = "QueryGen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.generate.clicked.connect(self.get_query)

    def get_query(self):
        self.textbox.clear()
        range_spinbox = int(self.spinbox.value())
        for x in range(range_spinbox):
            first_name = Name_Generator.genfn()
            middle_name = Name_Generator.genfn()
            last_name = Name_Generator.genln()
            username = first_name + str(random.randint(1, 999))
            mail = username + EmailGen.gen_mail()
            name = first_name + " " + middle_name
            self.textbox.appendPlainText(
                "INSERT INTO `login` (`FName`, `LName`, `Username`, `Mail`) VALUES ('" + name + "', '" + last_name + "', '" + username + "', '" + mail + "');")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

# Generate First Name
# Name_Generator.genfn()

# Generate Last Name
# Name_Generator.genln()

# Generate Password (Length of the pass)
# PassGen.GenPass(10)

# Generate Email Domain (Length of the pass)
# EmailGen.gen_mail()

