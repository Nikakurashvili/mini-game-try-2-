from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, 
                             QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout)
from random import randint, choice
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import os
import sys

class main_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3gaRAMa')
        self.setStyleSheet("background-color:blue")
        grid_layout=QGridLayout()

        button_tic_tac_toe=QPushButton('Tic-tac-toe')
        button_tic_tac_toe.setStyleSheet('background-color:cyan')
        button_tic_tac_toe.setFixedHeight(60)
        button_tic_tac_toe.setFixedWidth(500)
        button_tic_tac_toe.clicked.connect(self.show_tic_tac_toe)

        button_rock_paper_scissors=QPushButton('rock paper scissors')
        button_rock_paper_scissors.setStyleSheet('background-color:cyan')
        button_rock_paper_scissors.setFixedHeight(60)
        button_rock_paper_scissors.clicked.connect(self.show_rock_paper_scissors)
        
        button_guess_the_number=QPushButton('guess the number')
        button_guess_the_number.setStyleSheet('background-color:cyan')
        button_guess_the_number.setFixedHeight(60)
        button_guess_the_number.clicked.connect(self.show_game_num)

        exit=QPushButton('exit')
        exit.setStyleSheet('background-color:grey, color:black')
        exit.setFixedHeight(60)
        exit.clicked.connect(self.close)

        mute=QRadioButton('mute')
        mute.setStyleSheet('color: white')
        mute.toggled.connect(lambda: self.player.setVolume(0) if mute.isChecked() else self.player.setVolume(50))

        labe1=QLabel()
        self.player = QMediaPlayer()

        path = os.path.join(os.getcwd(), "main_menu_song.mp3")
        url = QUrl.fromLocalFile(path)  # works everywhere

        self.player.setMedia(QMediaContent(url))
        self.player.setVolume(50)
        self.player.play()

        def loop_song(status):
            if status == QMediaPlayer.EndOfMedia:
                self.player.setPosition(0)
                self.player.play()

        self.player.mediaStatusChanged.connect(loop_song)

        grid_layout.addWidget(labe1,0,0)
        grid_layout.addWidget(button_tic_tac_toe,0,1)
        grid_layout.addWidget(labe1,0,2)
        grid_layout.addWidget(labe1,1,0)
        grid_layout.addWidget(button_rock_paper_scissors,1,1)
        grid_layout.addWidget(labe1,1,2)
        grid_layout.addWidget(labe1,2,0)
        grid_layout.addWidget(button_guess_the_number,2,1)
        grid_layout.addWidget(labe1,2,2)
        grid_layout.addWidget(labe1,3,0)
        grid_layout.addWidget(exit,3,1)
        grid_layout.addWidget(labe1,3,2)
        grid_layout.addWidget(mute,4,0)
        grid_layout.addWidget(labe1,4,1)
        grid_layout.addWidget(labe1,4,2)

        self.setLayout(grid_layout)
        self.showMaximized()
    
    def show_game_num(self):
        self.game_num_window = game_num()
        self.game_num_window.show()
        self.hide()
        self.player.stop()

    def show_rock_paper_scissors(self):
        self.rock_paper_scissors_window = game_jeirani()
        self.rock_paper_scissors_window.show()
        self.hide()
        self.player.stop()

    def show_tic_tac_toe(self):
        self.rock_paper_scissors_window = game_tic_tac_toe()
        self.rock_paper_scissors_window.show()
        self.hide()
        self.player.stop()



class game_num(QWidget):
    def __init__(self):
        super().__init__()
        self.lucky_num = randint(1, 10)
        self.setStyleSheet('background-color:blue')
        grid_layout = QGridLayout()

        self.game_title = QLabel('\t  guess the number game')
        self.game_title.setStyleSheet('background-color:cyan')
        self.game_title.setFixedHeight(60)
        self.game_title.setFixedWidth(500)
        self.game_title.setFont(QFont('arial',16))
        
        restart=QPushButton('restart')
        restart.setFixedHeight(60)
        def res():
            self.button_guess_the_number.setPlaceholderText('enter a num(1-10): ')
            self.button_guess_the_number.setEnabled(True)
            self.button_guess_the_number.clear()
            self.lucky_num = randint(1, 10)                  
        restart.clicked.connect(res)
        restart.setFont(QFont('arial',16))

        self.button_guess_the_number=QLineEdit()
        self.button_guess_the_number.setPlaceholderText('enter a num(1-10): ')
        self.button_guess_the_number.setStyleSheet('background-color:white')
        self.button_guess_the_number.setFixedHeight(60)
        self.button_guess_the_number.setFixedWidth(500)

        mute=QRadioButton('mute')
        mute.setStyleSheet('color: white')
        mute.toggled.connect(lambda: self.player.setVolume(0) if mute.isChecked() else self.player.setVolume(50))

        main_menu=QPushButton('main menu')
        main_menu.setFixedHeight(60)
        main_menu.setFont(QFont('arial',14))
        main_menu.clicked.connect(self.show_main_menu)

        submit=QPushButton('submit')
        submit.setFixedHeight(60)
        submit.setFont(QFont('arial',14))
        submit.clicked.connect(self.check_guess)

        labe1=QLabel()

        self.player = QMediaPlayer()

        path = os.path.join(os.getcwd(), "guess_num_song.mp3")
        url = QUrl.fromLocalFile(path)  # works everywhere

        self.player.setMedia(QMediaContent(url))
        self.player.setVolume(50)
        self.player.play()
        self.player.setPosition(1000) 


        def loop_song(status):
            if status == QMediaPlayer.EndOfMedia:
                self.player.setPosition(1000) 
                self.player.play()

        self.player.mediaStatusChanged.connect(loop_song)

        grid_layout.addWidget(labe1,0,0)
        grid_layout.addWidget(self.game_title,0,1)
        grid_layout.addWidget(labe1,0,2)
        grid_layout.addWidget(labe1,1,0)
        grid_layout.addWidget(self.button_guess_the_number,1,1)
        grid_layout.addWidget(labe1,1,2)
        grid_layout.addWidget(labe1,2,0)
        grid_layout.addWidget(submit,2,1)
        grid_layout.addWidget(labe1,2,2)
        grid_layout.addWidget(labe1,3,0)
        grid_layout.addWidget(restart,3,1)
        grid_layout.addWidget(labe1,3,2)
        grid_layout.addWidget(mute,4,0)
        grid_layout.addWidget(main_menu,4,1)
        grid_layout.addWidget(labe1,4,2)

        self.setLayout(grid_layout)
        self.showMaximized()
    
    def check_guess(self):
        try:
            entered_num = int(self.button_guess_the_number.text())
            
            if entered_num < 1 or entered_num > 10:
                self.button_guess_the_number.setPlaceholderText('number out of range, enter a num(1-10): ')
                self.button_guess_the_number.clear()
                return
            
            if entered_num > self.lucky_num:
                self.button_guess_the_number.setPlaceholderText(f"{entered_num} is too high, try something lower")
            elif entered_num < self.lucky_num:
                self.button_guess_the_number.setPlaceholderText(f"{entered_num} is too low, try something higher")
            else:
                self.button_guess_the_number.setPlaceholderText(f"you guessed it, number was {self.lucky_num}")
                self.button_guess_the_number.setEnabled(False)
                self.lucky_num = randint(1, 10)                  
            self.button_guess_the_number.clear()
            
        except ValueError:
            self.button_guess_the_number.setPlaceholderText('enter a num(1-10): ')
            self.button_guess_the_number.clear()
    
    def show_main_menu(self):
        self.main_menu_window = main_menu()
        self.main_menu_window.show()
        self.hide()
        self.player.stop()




class game_jeirani(QWidget):
    def __init__(self):
        super().__init__()
        self.moves = ['rock', 'paper', 'scissors']
        self.pc_move = choice(self.moves)
        self.setStyleSheet('background-color:blue')
        grid_layout = QGridLayout()

        self.game_title = QLabel('\t     rock paper scissors')
        self.game_title.setStyleSheet('background-color:cyan')
        self.game_title.setFixedHeight(60)
        self.game_title.setFixedWidth(500)
        self.game_title.setFont(QFont('arial',16))
        
        self.restart=QPushButton('restart')
        self.restart.setFixedHeight(60)

        self.result_shower=QLineEdit()
        self.result_shower.setPlaceholderText('make a move(click the button): ')
        self.result_shower.setStyleSheet('background-color:white')
        self.result_shower.setFixedHeight(60)
        self.result_shower.setFixedWidth(500)
        self.result_shower.setDisabled(True)

        mute=QRadioButton('mute')
        mute.setStyleSheet('color: white')

        main_menu=QPushButton('main menu')
        main_menu.setFixedHeight(60)
        main_menu.setFont(QFont('arial',14))
        main_menu.clicked.connect(self.show_main_menu)

        buttons_3=QHBoxLayout()
        self.rock_button=QPushButton('rock')
        self.rock_button.setFixedHeight(60)
        self.rock_button.clicked.connect(self.make_move)

        self.paper_button=QPushButton('paper')
        self.paper_button.setFixedHeight(60)
        self.paper_button.clicked.connect(self.make_move)

        self.scissors_button=QPushButton('scissors')
        self.scissors_button.setFixedHeight(60)
        self.scissors_button.clicked.connect(self.make_move)
        
        buttons_3.addWidget(self.rock_button)
        buttons_3.addWidget(self.paper_button)
        buttons_3.addWidget(self.scissors_button)

        labe1=QLabel()

        mute=QRadioButton('mute')
        mute.setStyleSheet('color: white')
        mute.toggled.connect(lambda: self.player.setVolume(0) if mute.isChecked() else self.player.setVolume(50))

        self.player = QMediaPlayer()

        path = os.path.join(os.getcwd(), "rock_paper_scissors_song.mp3")
        url = QUrl.fromLocalFile(path)  

        self.player.setMedia(QMediaContent(url))
        self.player.setVolume(50)
        self.player.play()

        def loop_song(status):
            if status == QMediaPlayer.EndOfMedia:
                self.player.setPosition(0)
                self.player.play()
        self.player.mediaStatusChanged.connect(loop_song)


        grid_layout.addWidget(labe1,0,0)
        grid_layout.addWidget(self.game_title,0,1)
        grid_layout.addWidget(labe1,0,2)
        grid_layout.addWidget(labe1,1,0)
        grid_layout.addWidget(self.result_shower,1,1)
        grid_layout.addWidget(labe1,1,2)
        grid_layout.addWidget(labe1,2,0)
        grid_layout.addLayout(buttons_3,2,1)
        grid_layout.addWidget(labe1,2,2)
        grid_layout.addWidget(labe1,3,0)
        grid_layout.addWidget(self.restart,3,1)
        grid_layout.addWidget(labe1,3,2)
        grid_layout.addWidget(mute,4,0)
        grid_layout.addWidget(main_menu,4,1)
        grid_layout.addWidget(labe1,4,2)

        self.setLayout(grid_layout)
        self.showMaximized()
    
        self.restart.clicked.connect(self.res)
        self.restart.setFont(QFont('arial',16))

    def res(self):
        self.result_shower.setPlaceholderText('make a move(click the button): ')
        self.result_shower.clear()
        self.pc_move = choice(self.moves)
        self.rock_button.setEnabled(True)
        self.paper_button.setEnabled(True)
        self.scissors_button.setEnabled(True)

    def make_move(self):
        s = self.sender()
        my_move = s.text()
        self.result_shower.setPlaceholderText(f"you: {my_move}, computer: {self.pc_move}")

        if my_move == 'rock' and self.pc_move == 'paper':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: pc")
        elif my_move == 'rock' and self.pc_move == 'scissors':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: you")
        elif my_move == 'scissors' and self.pc_move == 'rock':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: pc")
        elif my_move == 'scissors' and self.pc_move == 'paper':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: you")
        elif my_move == 'paper' and self.pc_move == 'rock':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: you")
        elif my_move == 'paper' and self.pc_move == 'scissors':
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  winner: pc")
        else:
            self.result_shower.setPlaceholderText(f"you: {my_move},  computer: {self.pc_move},  result: draw!")
            
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissors_button.setEnabled(False)
        self.pc_move = choice(self.moves)

    def show_main_menu(self):
        self.main_menu_window = main_menu()
        self.main_menu_window.show()
        self.hide()
        self.player.stop()








class game_tic_tac_toe(QWidget):
    def __init__(self):
        super().__init__()

        self.current_player = 'X'  
        self.board = [''] * 9 
        self.game_over = False

        self.setStyleSheet('background-color:blue')
        grid_layout = QGridLayout()

        self.game_title = QLabel('\t     tic-tac-toe')
        self.game_title.setStyleSheet('background-color:cyan')
        self.game_title.setFixedHeight(60)
        self.game_title.setFixedWidth(400)
        self.game_title.setFont(QFont('arial',16))
        
        restart = QPushButton('restart')
        restart.setFixedHeight(60)
        restart.clicked.connect(self.reset_game)
        restart.setFont(QFont('arial',16))

        mute=QRadioButton('mute')
        mute.setStyleSheet('color: white')
        mute.toggled.connect(lambda: self.player.setVolume(0) if mute.isChecked() else self.player.setVolume(50))

        main_menu = QPushButton('main menu')
        main_menu.setFixedHeight(60)
        main_menu.setFont(QFont('arial',14))
        main_menu.clicked.connect(self.show_main_menu)

        self.tic_buttons = []
        for i in range(9):
            button = QPushButton()
            button.setFixedHeight(120)
            button.setFixedWidth(400)
            button.setFont(QFont('arial', 48))  
            button.clicked.connect(lambda _, idx=i: self.make_move(idx))
            self.tic_buttons.append(button)





        self.player = QMediaPlayer()

        path = os.path.join(os.getcwd(), "tic_tac_toe_song.mp3")
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



        grid_layout.addWidget(self.game_title, 0, 1)

        grid_layout.addWidget(self.tic_buttons[0], 1, 0)
        grid_layout.addWidget(self.tic_buttons[1], 1, 1)
        grid_layout.addWidget(self.tic_buttons[2], 1, 2)
        grid_layout.addWidget(self.tic_buttons[3], 2, 0)
        grid_layout.addWidget(self.tic_buttons[4], 2, 1)
        grid_layout.addWidget(self.tic_buttons[5], 2, 2)
        grid_layout.addWidget(self.tic_buttons[6], 3, 0)
        grid_layout.addWidget(self.tic_buttons[7], 3, 1)
        grid_layout.addWidget(self.tic_buttons[8], 3, 2)

        grid_layout.addWidget(mute, 4, 0)
        grid_layout.addWidget(main_menu, 4, 1)
        grid_layout.addWidget(restart, 4, 2)

        self.setLayout(grid_layout)
        self.showMaximized()
    
    def make_move(self, position):
        if self.game_over or self.board[position] != '':
            return
            
        self.board[position] = self.current_player
        self.tic_buttons[position].setText(self.current_player)
        
        if self.check_winner():
            self.game_title.setText(f"                Player {self.current_player} wins!")
            self.game_over = True
        elif '' not in self.board:
            self.game_title.setText("                    It's a tie!")
            self.game_over = True
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != '':
                return True
        
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != '':
                return True
        
        if self.board[0] == self.board[4] == self.board[8] != '':
            return True
        if self.board[2] == self.board[4] == self.board[6] != '':
            return True
        return False
    
    def reset_game(self):
        self.current_player = 'X'
        self.board = [''] * 9
        self.game_over = False
        self.game_title.setText('\t     tic-tac-toe')
        for button in self.tic_buttons:
            button.setText('')

    def show_main_menu(self):
        self.main_menu_window = main_menu()
        self.main_menu_window.show()
        self.hide()
        self.player.stop()



app = QApplication(sys.argv)
window = main_menu()
sys.exit(app.exec_())