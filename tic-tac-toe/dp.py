from tic_tac_toe import TicTacToe

class TicTacToeDP:
    def __init__(self, size=4):
        self.game = TicTacToe(size)
        self.state_values = {}  # Stores the value of each state

    def get_state(self):
        return tuple(map(tuple, self.game.board))  # Convert board to immutable state

    def value(self, state, player):
        if self.game.check_win(player):
            return 1  # Win for the player
        if self.game.check_win(-player):
            return -1  # Loss for the player
        if self.game.is_full():
            return 0  # Draw
        
        state_key = (state, player)
        if state_key in self.state_values:
            return self.state_values[state_key]

        # Recurse over possible moves
        best_value = -float('inf') if player == 1 else float('inf')
        for move in self.game.available_moves():
            self.game.make_move(move[0], move[1], player)
            next_state = self.get_state()
            move_value = self.value(next_state, -player)
            self.game.board[move[0], move[1]] = 0  # Undo move

            if player == 1:
                best_value = max(best_value, move_value)
            else:
                best_value = min(best_value, move_value)

        self.state_values[state_key] = best_value
        return best_value
