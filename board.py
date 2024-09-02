class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def minimax(self, depth, is_maximizing):
        if self.check_winner('X'):
            return -1
        if self.check_winner('O'):
            return 1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = -float('inf')
        best_move = ()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def human_move(self):
        while True:
            try:
                row = int(input("Enter row (1, 2, 3): ")) - 1
                col = int(input("Enter column (1, 2, 3): ")) - 1
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    break
                else:
                    print("This spot is already taken!")
            except (IndexError, ValueError):
                print("Invalid input! Please enter numbers between 1 and 3.")

    def play_game(self):
        while True:
            self.print_board()

            # Human player move
            self.human_move()
            if self.check_winner('X'):
                self.print_board()
                print("Player X wins!")
                break
            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                break

            # AI move
            ai_move = self.find_best_move()
            if ai_move:
                self.board[ai_move[0]][ai_move[1]] = 'O'
            if self.check_winner('O'):
                self.print_board()
                print("AI wins!")
                break
            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                break


# Start the game
game = TicTacToe()
game.play_game()