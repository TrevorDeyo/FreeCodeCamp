import random
from collections import Counter

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    moves_counter = Counter(opponent_history)

    moves = ["R", "P", "S"]

    if prev_play == "":
        guess = random.choice(moves)
    else:
        predicted_move = max(moves_counter, key=lambda k: moves_counter[k])
        if predicted_move == "":
            guess = random.choice(moves)
        else:
            index_in_moves = moves.index(predicted_move)
            next_index = (index_in_moves + 1) % len(moves)
            guess = moves[next_index]

    return guess