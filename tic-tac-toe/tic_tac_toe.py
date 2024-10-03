import numpy as np
import random

class TicTacToe:
    def __init__(self, size=4):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)  # 0: empty, 1: X, -1: O

    def reset(self):
        self.board = np.zeros((self.size, self.size), dtype=int)

    def check_win(self, player):
        # Check rows, columns, and diagonals for win
        for i in range(self.size):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        # Check diagonals
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def is_full(self):
        return np.all(self.board != 0)

    def available_moves(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i, j] == 0]

    def make_move(self, row, col, player):
        if self.board[row, col] == 0:
            self.board[row, col] = player
            return True
        return False
