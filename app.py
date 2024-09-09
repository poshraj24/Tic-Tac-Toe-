from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/static')

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def check_winner(self, player):
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

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

game = TicTacToe()

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    print(f"Received move: {data}")  # Debugging log
    row = data['row']
    col = data['col']
    player = data['player']

    if game.make_move(row, col, player):
        if game.check_winner(player):
            return jsonify({"status": "win", "board": game.board})
        elif game.check_draw():
            return jsonify({"status": "draw", "board": game.board})
        else:
            ai_move = game.find_best_move()
            if ai_move:
                game.make_move(ai_move[0], ai_move[1], 'O')
                if game.check_winner('O'):
                    return jsonify({"status": "lose", "board": game.board})
                elif game.check_draw():
                    return jsonify({"status": "draw", "board": game.board})
            return jsonify({"status": "continue", "board": game.board})
    else:
        return jsonify({'board': game.board, 'status': 'continue'})

@app.route('/reset', methods=['POST'])
def reset():
    global game
    game = TicTacToe()
    return jsonify({"status": "reset", "board": game.board})

@app.route('/')
def index():
    return render_template('index.html')  # Corrected the path

if __name__ == '__main__':
    app.run(debug=True)
