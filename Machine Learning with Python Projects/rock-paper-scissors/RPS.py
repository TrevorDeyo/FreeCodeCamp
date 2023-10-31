def player(prev_play, opponent_history=[]):
    # If a previous play is available, add it to the opponent's history
    if prev_play:
        opponent_history.append(prev_play)
    else:
        # Clear the opponent's history when the game resets
        opponent_history.clear()

    # Define a mapping for countering moves
    counter_moves = { 'R': 'P', 'P': 'S', 'S': 'R' }

    # Initialize the computer's guess as "S" (Scissors)
    guess = "S"

    # Check if there are enough moves in the opponent's history for predictions
    if len(opponent_history) >= 4:
        # Create a list of the last four-move sequences in opponent's history
        play_order = [ ''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3]) ]

        # Generate potential next plays by appending 'S', 'R', 'P' to the last three moves
        potential_plays = [ ''.join([ *opponent_history[-3:], v ]) for v in ['S', 'R', 'P'] ]

        # Create a sub-order dictionary with the count of each potential play
        sub_order = { k: play_order.count(k) for k in potential_plays }

        # Predict the next opponent move based on the most frequent sequence
        predicted_move = max(sub_order, key=sub_order.get)[-1]

        # Use the counter_moves mapping to choose a move to counter the prediction
        guess = counter_moves[predicted_move]

    # Return the computer's guess
    return guess
