from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import webbrowser
def launch():
    webbrowser.open("https://deadshot.io/")
#-----------------------------------------------------------------------


app = QApplication([])
mainwin = QWidget()
mainwin.setWindowTitle('DeadShot Launcher 0.2')

mainwin.resize(400,200)

textWin = QLabel("Launch Game")
creator = QLabel("Launcher by MrMeRKa")

button = QPushButton("Launch")


v_line = QVBoxLayout()
v_line.addWidget(textWin, alignment = Qt.AlignCenter)
v_line.addWidget(creator, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
mainwin.setLayout(v_line)
button.clicked.connect(launch)

mainwin.show()
app.exec_()