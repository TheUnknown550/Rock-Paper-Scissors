import random

def player(prev_play, opponent_history=[]):
    # Default move
    guess = 'R'
    
    # Keeping track of the history
    if prev_play != "": # if we haven't played yet
        opponent_history.append(prev_play)
    
    # If history is empty use the default guess
    if not opponent_history:
        return guess    

    # Strategy 1: Random choice
    guess = random.choice(['R', 'P', 'S'])
         
    # Strategy Quincy: Strategy to beat Quincy
    tenMoves = opponent_history[-10:]
    most_move = max(set(tenMoves), key=tenMoves.count)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = ideal_response[most_move]
    
    return guess
