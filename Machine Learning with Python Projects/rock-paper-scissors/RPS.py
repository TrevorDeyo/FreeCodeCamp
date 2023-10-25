from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Define global variables to store the computer's guess and opponent's last move
last_com_guess = None
opp_last_move = None

def player(prev_play, opponent_history=[]):
    global last_com_guess, opp_last_move

    if prev_play != '':
        # Update opponent's move
        opponent_history.append(prev_play)
        opp_last_move = prev_play

        # Map strings to ints
        char_to_num = {'R': 0, 'P': 1, 'S': 2}
        input_list = opponent_history
        numeric_list = [char_to_num[char] for char in input_list]

        # Convert to a 2D np array because sklearn.tree expects it to be
        moves = np.array(numeric_list).reshape(-1, 1)

        # Map outcomes to numeric values
        outcomes = []
        # ties
        if last_com_guess == opp_last_move:
            outcomes.append(2)  # Numeric value for tie
        # computer wins
        elif (last_com_guess == 1 and char_to_num[opp_last_move] == 0) or (last_com_guess == 0 and char_to_num[opp_last_move] == 2) or (
            last_com_guess == 2 and char_to_num[opp_last_move] == 1):
            outcomes.append(0)  # Numeric value for win
        # computer loses
        else:
            outcomes.append(1)  # Numeric value for lose

        clf = DecisionTreeClassifier()
        clf.fit(moves, outcomes)

        # Make a prediction
        guess = clf.predict([char_to_num[prev_play]])

        # Update the last_com_guess for the next round
        last_com_guess = guess
    else:
        # Handle the case where prev_play is empty (first game)
        opponent_history = ['']  # Initialize opponent history with an empty move
        opp_last_move = ''
        numeric_list = [3]  # Map the empty move to the integer 3

        # Convert to a 2D np array for the initial case
        moves = np.array(numeric_list).reshape(-1, 1)

        # For the first game, make an initial guess (e.g., 'R')
        guess = 'P'
    
    return guess