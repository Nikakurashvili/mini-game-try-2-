from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import os
from davaleba import Ui_Ui_MainWindow 

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.lucky_num = randint(1, 10)

        self.player = QMediaPlayer()
        path = os.path.join(os.getcwd(), "guess_num_song.mp3")
        if os.path.exists(path):
            url = QUrl.fromLocalFile(path)
            self.player.setMedia(QMediaContent(url))
            self.player.setVolume(50)
            self.player.play()
            self.player.setPosition(1000)
            
            def loop_song(status):
                if status == QMediaPlayer.EndOfMedia:
                    self.player.setPosition(1000)
                    self.player.play()
            
            self.player.mediaStatusChanged.connect(loop_song)

        self.ui.restart.clicked.connect(self.res)
        self.ui.mute.toggled.connect(self.toggle_mute)
        self.ui.exit.clicked.connect(self.close)
        self.ui.submit.clicked.connect(self.check_guess)

    def res(self):
        self.ui.button_guess_the_number.setPlaceholderText('enter a num(1-10): ')
        self.ui.button_guess_the_number.setEnabled(True)
        self.ui.button_guess_the_number.clear()
        self.lucky_num = randint(1, 10)

    def toggle_mute(self):
        if self.ui.mute.isChecked():
            self.player.setVolume(0)
        else:
            self.player.setVolume(50)

    def check_guess(self):
        try:
            entered_num = int(self.ui.button_guess_the_number.text())
            
            if entered_num < 1 or entered_num > 10:
                self.ui.button_guess_the_number.setPlaceholderText('number out of range, enter a num(1-10): ')
                self.ui.button_guess_the_number.clear()
                return
            
            if entered_num > self.lucky_num:
                self.ui.button_guess_the_number.setPlaceholderText(f"{entered_num} is too high, try something lower")
            elif entered_num < self.lucky_num:
                self.ui.button_guess_the_number.setPlaceholderText(f"{entered_num} is too low, try something higher")
            else:
                self.ui.button_guess_the_number.setPlaceholderText(f"you guessed it, number was {self.lucky_num}")
                self.ui.button_guess_the_number.setEnabled(False)
                self.lucky_num = randint(1, 10)
            self.ui.button_guess_the_number.clear()
            
        except ValueError:
            self.ui.button_guess_the_number.setPlaceholderText('enter a num(1-10): ')
            self.ui.button_guess_the_number.clear()

app = QApplication(sys.argv)
window = MyApp()
window.showMaximized()
sys.exit(app.exec_())


