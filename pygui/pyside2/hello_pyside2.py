# hello_pyside2.py
""" Hello World in PySide2 """
import sys
from PySide2.QtWidgets import QApplication, QLabel

def main():
    app = QApplication(sys.argv)
    #label = QLabel("Hello World")
    #saludo = "Hello PySide2"
    #saludo = sys.argv[1]
    saludo = f"<font color=red size=40>{sys.argv[1]}</font>"
    label = QLabel(saludo)
    label.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
