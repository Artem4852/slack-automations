import sys, os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QFontDatabase
from arcadeApi import ArcadeApi

def loadFont(filename, size=32, weight=400):
    if os.path.exists(filename): 
        font_id = QFontDatabase.addApplicationFont(filename)
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
    else: family = filename
    return QFont(family, size, weight)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arcade Sessions Automation")
        self.setStyleSheet("""
    QMainWindow { background-color : #FAEFD6; color : #FF8C37; }
    QLabel { color : #FF8C37; }
    QPushButton { background-color : #0AAFB4; color : #FAEFD6; border-radius : 5px; padding : 0 10px; }
    QLineEdit { background-color : #0AAFB4; color : #FAEFD6; border-radius : 5px; padding : 0 10px; }""")
        self.arcadeApi = ArcadeApi(user_id="U07BBJR072P", save=True, debug=False)
        self.setup_ui()

    def setup_ui(self):
        self.resize(600, 800)

        # Font at Slackey/Slackey-Regular.ttf
        self.fontHeading = loadFont("Open Sans", 32, 700)
        self.fontText = loadFont("Open Sans", 16, 400)

        self.window_title = QLabel("Interact with Arcade without Slack", self)
        self.window_title.setFont(self.fontHeading)
        self.window_title.adjustSize()

        start_x = 300-self.window_title.width()//2


        self.button_start_session = QPushButton("Start session", self)
        self.button_start_session.resize(100, 30)
        self.button_start_session.clicked.connect(self.start_session)

        self.label_session_title = QLabel("Session title:", self)
        self.label_session_title.setFont(self.fontText)
        self.label_session_title.adjustSize()

        self.input_session_title = QLineEdit(self)
        self.input_session_title.resize(400, 30)

        self.window_title.move(start_x, 50)
        self.label_session_title.move(start_x, self.window_title.pos().y()+self.window_title.height()+20)
        self.input_session_title.move(start_x, self.label_session_title.pos().y()+self.label_session_title.height()+5)
        self.button_start_session.move(start_x, self.input_session_title.pos().y()+self.input_session_title.height()+30)

    def start_session(self):
        title = self.input_session_title.text()
        if not title: self.label_session_title.setText("Session title: Please enter a title"); self.label_session_title.repaint(); return
        try: self.arcadeApi.start_session(title)
        except Exception as e: self.label_session_title.setText(f"Session title: {e}"); self.label_session_title.repaint();

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())