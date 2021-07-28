import sys
import webbrowser
from PyQt6.QtWidgets import QApplication, QDialog
from ui_zakaz1 import Ui_zakaz

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_zakaz()
ui.setupUi(window)


#webbrowser.open("https://konovalov.top/index.php/ssylki.html")

window.show()
sys.exit(app.exec())
