from PyQt6 import QtWidgets
from Login.login import LoginApp
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


# END