import matplotlib.pyplot as plt
from dp import TicTacToeDP

def simulate_games(agent, num_games=10):
    win_count = 0
    total_games = 0
    win_rates = []

    for _ in range(num_games):
        agent.game.reset()
        player = 1  # X always starts
        state = agent.get_state()

        while not agent.game.is_full():
            # Choose best move for the current player using DP
            moves = agent.game.available_moves()
            best_move = None
            best_value = -float('inf') if player == 1 else float('inf')

            for move in moves:
                agent.game.make_move(move[0], move[1], player)
                next_state = agent.get_state()
                move_value = agent.value(next_state, -player)
                agent.game.board[move[0], move[1]] = 0  # Undo move

                if (player == 1 and move_value > best_value) or (player == -1 and move_value < best_value):
                    best_value = move_value
                    best_move = move

            # Make the best move
            agent.game.make_move(best_move[0], best_move[1], player)
            state = agent.get_state()

            if agent.game.check_win(player):
                if player == 1:
                    win_count += 1
                total_games += 1
                break

            player = -player  # Switch players

        win_rate = win_count / (total_games if total_games != 0 else 1)
        win_rates.append(win_rate)

    return win_rates


def main():
    # Run the simulation for a 4x4 board
    agent = TicTacToeDP(size=3)
    win_rates = simulate_games(agent, num_games=10)

    # Plotting
    plt.plot(win_rates)
    plt.title("Win Rate of DP Agent vs Random Player (4x4)")
    plt.xlabel("Game Number")
    plt.ylabel("Win Rate")
    plt.show()

if __name__=="__main__":
    main()