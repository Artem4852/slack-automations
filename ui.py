import sys, os, json
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QMessageBox
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
        max_width = self.window_title.width()

        # self.button_load_session = QPushButton("Load session", self)
        # self.button_load_session.resize(max_width//2-20, 30)
        # self.button_load_session.clicked.connect(self.load_session)

        self.label_session_title = QLabel("Session title:", self)
        self.label_session_title.setFont(self.fontText)
        self.label_session_title.adjustSize()

        self.input_session_title = QLineEdit(self)
        self.input_session_title.resize(max_width, 30)

        self.label_session_length = QLabel("Session length [h:m]:", self)
        self.label_session_length.setFont(self.fontText)
        self.label_session_length.adjustSize()

        self.input_session_length = QLineEdit(self)
        self.input_session_length.resize(max_width, 30)

        self.label_directory_path = QLabel("Absolute path to your working directory:", self)
        self.label_directory_path.setFont(self.fontText)
        self.label_directory_path.adjustSize()

        self.input_directory_path = QLineEdit(self)
        self.input_directory_path.resize(max_width, 30)

        self.button_start_session = QPushButton("Start session", self)
        self.button_start_session.resize(max_width//2-20, 30)
        self.button_start_session.clicked.connect(self.start_session)

        self.button_pause_session = QPushButton("Pause", self)
        self.button_pause_session.resize(max_width//2-20, 30)
        self.button_pause_session.clicked.connect(self.pause_session)

        self.button_resume_session = QPushButton("Resume", self)
        self.button_resume_session.resize(max_width//2-20, 30)
        self.button_resume_session.clicked.connect(self.resume_session)

        self.label_reply = QLabel("Message to be sent to thread:", self)
        self.label_reply.setFont(self.fontText)
        self.label_reply.adjustSize()

        self.input_reply = QLineEdit(self)
        self.input_reply.resize(max_width, 30)

        self.button_send_reply = QPushButton("Send to thread", self)
        self.button_send_reply.resize(max_width//2-20, 30)
        self.button_send_reply.clicked.connect(self.post_reply)

        self.window_title.move(start_x, 50)
        self.label_session_title.move(start_x, self.window_title.pos().y()+self.window_title.height()+20)
        self.input_session_title.move(start_x, self.label_session_title.pos().y()+self.label_session_title.height()+5)
        self.label_session_length.move(start_x, self.input_session_title.pos().y()+self.input_session_title.height()+20)
        self.input_session_length.move(start_x, self.label_session_length.pos().y()+self.label_session_length.height()+5)
        self.label_directory_path.move(start_x, self.input_session_length.pos().y()+self.input_session_length.height()+20)
        self.input_directory_path.move(start_x, self.label_directory_path.pos().y()+self.label_directory_path.height()+5)

        self.button_start_session.move(start_x, self.input_directory_path.pos().y()+self.input_directory_path.height()+30)
        # self.button_load_session.move(start_x+self.button_start_session.width()+40, self.input_session_title.pos().y()+self.input_session_title.height()+30)
        self.button_pause_session.move(start_x, self.button_start_session.pos().y()+self.button_start_session.height()+30)
        self.button_resume_session.move(start_x+self.button_pause_session.width()+40, self.button_start_session.pos().y()+self.button_start_session.height()+30)

        self.label_reply.move(start_x, self.button_pause_session.pos().y()+self.button_pause_session.height()+30)
        self.input_reply.move(start_x, self.label_reply.pos().y()+self.label_reply.height()+5)
        self.button_send_reply.move(start_x, self.input_reply.pos().y()+self.input_reply.height()+10)

    def start_session(self):    
        title = self.input_session_title.text()
        length = self.input_session_length.text()
        directory_path = self.input_directory_path.text()
        if not title: 
            self.show_error_message("Please enter a session title")
            return

        if not length:
            self.show_error_message("Please enter a session length")
            return

        length_parts = length.split(":")
        if len(length_parts) != 2 or not all(part.isdigit() for part in length_parts):
            self.show_error_message("Please enter a valid session length in h:m format")
            return
        

        if not directory_path:
            self.show_error_message("Please enter a directory path")
            return

        if not os.path.exists(directory_path):
            self.show_error_message("The specified directory does not exist")
            return

        self.go_to_directory()

        try:
            self.arcadeApi.start_session(title)
            self.label_session_title.setText(f"Session title: Session '{title}' started successfully")
        except Exception as e:
            error_message = str(e)
            self.label_session_title.setText(f"Session title: Error - {error_message}")
            self.show_error_message(f"Error starting session: {error_message}")

    def go_to_directory(self):
        os.system(f"cd {self.input_directory_path.text()}")
        with open(f"config.json", "w") as f:
            f.write(json.dumps({"title": self.input_session_title.text(), "length": self.input_session_length.text()}))

    def pause_session(self):
        print("pause")
        try: 
            self.arcadeApi.pause_session()
        except Exception as e: 
            if not self.arcadeApi.current_session_ts:
                self.show_error_message("Start a session first")
                return
            elif self.arcadeApi.paused:
                self.show_error_message("Session is paused already")
                return
            self.show_error_message(f"Unexpected exception: {str(e)}")
            
    def resume_session(self):
        print("resume")
        try:
            self.arcadeApi.resume_session()
        except Exception as e:
            if not self.arcadeApi.current_session_ts:
                self.show_error_message("Start a session first")
                return
            elif not self.arcadeApi.paused:
                self.show_error_message("Session is not paused")
                return
            self.show_error_message(f"Unexpected exception: {str(e)}")
            
    def post_reply(self):
        text = self.input_reply.text()
        if not text:
            self.show_error_message("Message cannot be empty")
            return
        try:
            self.arcadeApi.post_reply(text)
        except:
            if not self.arcadeApi.current_session_ts:
                self.show_error_message("Start a session first")
                return

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

    # def load_session(self):
    #     pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())