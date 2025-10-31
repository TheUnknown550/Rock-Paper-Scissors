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
         
    
    return guess
