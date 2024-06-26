import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player1_icon = 'X'
        self.player2_icon = 'O'
        self.current_player = self.player1_icon
        self.winner = None

    def print_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    def check_win(self, icon):
        # Check all rows
        for i in range(0, 9, 3):
            if self.board[i] == icon and self.board[i + 1] == icon and self.board[i + 2] == icon:
                return True
        # Check all columns
        for i in range(3):
            if self.board[i] == icon and self.board[i + 3] == icon and self.board[i + 6] == icon:
                return True
        # Check both diagonals
        if self.board[0] == icon and self.board[4] == icon and self.board[8] == icon:
            return True
        if self.board[2] == icon and self.board[4] == icon and self.board[6] == icon:
            return True
        return False

    def is_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False

    def basic_computer_move(self):
        icon = self.player2_icon
        # Check if the computer can win in the next move
        for i in range(0, 9):
                if self.board[i] == ' ':
                    self.board[i] = icon
                    if self.check_win(icon):
                        return
                    self.board[i] = ' '
        # Check if the player can win in the next move and block them
        for i in range(0, 9):
            if self.board[i] == ' ':
                self.board[i] = self.player1_icon
                if self.check_win(self.player1_icon):
                    self.board[i] = icon
                    return
                self.board[i] = ' '
        # Otherwise, make a random move
        while True:
            choice = random.randint(0, 8)
            if self.board[choice] == ' ':
                self.board[choice] = icon
                return

    def player_move(self, icon):
        if icon == self.player1_icon:
            print(f"Your turn player {self.player1_icon}")
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Please enter a value between 1 and 9.")
                self.player_move(icon)
                return
            if self.board[choice - 1] == ' ':
                self.board[choice - 1] = icon
            else:
                print()
                print("That space is already taken! Go again.")
                self.player_move(icon)
        else:
            print("Computer's turn")
            self.basic_computer_move()
            

    def play_game(self):
        while True:
            self.print_board()
            self.player_move('X')
            self.print_board()
            if self.check_win('X'):
                print("X wins! Congratulations!")
                break
            elif self.is_draw():
                print("It's a draw!")
                break
            self.player_move('O')
            if self.check_win('O'):
                self.print_board()
                print("O wins! Congratulations!")
                break
            elif self.is_draw():
                print("It's a draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()