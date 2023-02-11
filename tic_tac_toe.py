import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player1_icon = 'X'
        self.player2_icon = 'O'
        self.current_player = self.player1_icon
        self.winner = None

    def print_board(self):
        print(" {} | {} | {} ".format(self.board[0], self.board[1], self.board[2]))
        print("---+---+---")
        print(" {} | {} | {} ".format(self.board[3], self.board[4], self.board[5]))
        print("---+---+---")
        print(" {} | {} | {} ".format(self.board[6], self.board[7], self.board[8]))
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

    def player_move(self, icon):
        print(self.board)
        if icon == self.player1_icon:
            number = 1
        elif icon == self.player2_icon:
            number = 2
        if number == 1:
            print("Your turn player {}".format(number))
            choice = int(input("Enter your move (1-9): ").strip())
            if self.board[choice - 1] == ' ':
                self.board[choice - 1] = icon
                print(self.board)
            else:
                print()
                print("That space is already taken!")
        else:
            print("Computer's turn")
            # Check if the computer can win in the next move
            for i in range(0, 9):
                if self.board[i] == ' ':
                    self.board[i] = icon
                    print('check computer win')
                    print(self.board)
                    if self.check_win(icon):
                        return
                    self.board[i] = ' '
            # Check if the player can win in the next move and block them
            for i in range(0, 9):
                if self.board[i] == ' ':
                    self.board[i] = self.player1_icon
                    print('check player win')
                    print(self.board)
                    if self.check_win(self.player1_icon):
                        self.board[i] = icon
                        return
                    self.board[i] = ' '
            # Otherwise, make a random move
            while True:
                choice = random.randint(0, 8)
                if self.board[choice] == ' ':
                    self.board[choice] = icon
                    print('random move %d', choice)
                    print(self.board)
                    return

if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game.print_board()
        game.player_move('X')
        game.print_board()
        if game.check_win('X'):
            print("X wins! Congratulations!")
            break
        elif game.is_draw():
            print("It's a draw!")
            break
        game.player_move('O')
        if game.check_win('O'):
            game.print_board()
            print("O wins! Congratulations!")
            break
        elif game.is_draw():
            print("It's a draw!")
            break
