import random

def player(prev_play, opponent_history=[], my_history=[]):
    # Default move
    guess = 'R'
    
    # Keeping track of the history
    if prev_play != "": # if we haven't played yet
        opponent_history.append(prev_play)
    
    # If history is empty use the default guess
    if not opponent_history:
        return guess    
    
    # Map of counters & possible moves
    counter = {"R": "P", "P": "S", "S": "R"}
    moves = ["R", "P", "S"]

    # Strategy 1: Random choice
    # guess = random.choice(['R', 'P', 'S'])
    
    # Strategy Quincy: Strategy to beat Quincy; cyclic sequence > R, R, P, P, S, R, R, P, P, S,
    # choices = ["R", "R", "P", "P", "S"]
    # predicted = choices[len(opponent_history) % len(choices)]
    # guess = counter[predicted]
    
    # Strategy Mrugesh: Beat Mrugesh by predicting his counter to
    # myLastTen = my_history[-10:]
    # if not myLastTen:
        # predicted_my_move = 'R'
    # else:
        # predicted_my_move = max(set(myLastTen), key=myLastTen.count)
    # mrugesh_next = counter[predicted_my_move]
    # guess = counter[mrugesh_next]

    # Strategy Kris: Strategy to beat Kris; always plays what beats the last move.
    if my_history:
        kris_next = counter[my_history[-1]]
        guess = counter[kris_next]
    else:
        # Kris opens with 'P' (since he assumes our '' -> 'R'), so play 'S'
        guess = 'S'

    
    # Track our own move history for strategies that need it
    my_history.append(guess)
    return guess
