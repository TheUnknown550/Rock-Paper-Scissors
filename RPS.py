import random
from collections import defaultdict

def beat_Quincys(opponent_history): # 5-move repeat pattern R,R,P,P,S
    counter = {"R": "P", "P": "S", "S": "R"}
    choices = ["R", "R", "P", "P", "S"]
    predicted = choices[len(opponent_history) % len(choices)]
    return counter[predicted]

def beat_Mrugesh(my_history): # Plays what beats your most frequent
    counter = {"R": "P", "P": "S", "S": "R"}
    myLastTen = my_history[-10:]
    if not myLastTen:
        predicted_my_move = 'R'
    else:
        predicted_my_move = max(set(myLastTen), key=myLastTen.count)
    mrugesh_next = counter[predicted_my_move]
    return counter[mrugesh_next]

def beat_Kris(my_history): # Plays what beats your last move
    counter = {"R": "P", "P": "S", "S": "R"}
    if my_history:
        kris_next = counter[my_history[-1]]
        return counter[kris_next]
    else:
        # Kris opens with 'P' (since he assumes our '' -> 'R'), so play 'S'
        return 'S'
    
def beat_Abbeys(my_history): # Uses 2-move Markov prediction
    counter = {"R": "P", "P": "S", "S": "R"}
    if my_history:
        # Build transition counts: XY means we played X then Y
        play_order = defaultdict(int)
        for i in range(len(my_history) - 1):
            pair = my_history[i] + my_history[i + 1]
            play_order[pair] += 1
        last_my = my_history[-1]
    else:
        # Abbey treats empty prev as 'R'
        last_my = 'R'
        play_order = {}
    potential_plays = [last_my + 'R', last_my + 'P', last_my + 'S']
    best_pair = max(potential_plays, key=lambda k: play_order.get(k, 0))
    predicted_our_next = best_pair[-1]
    abbey_next = counter[predicted_our_next]
    return counter[abbey_next]


def pick_strategy(prev_play, opponent_history, my_history, state):
    counter = {"R": "P", "P": "S", "S": "R"}

    # Update expert weights based on last observed opponent move
    if prev_play != "" and state.get('last_suggestions'):
        for expert, move in state['last_suggestions'].items():
            if move == prev_play:
                continue  # tie, no change
            elif counter.get(move) == prev_play:
                state['weights'][expert] -= 1  # would have lost
            elif counter.get(prev_play) == move:
                state['weights'][expert] += 1  # would have won

    # Record opponent history
    if prev_play != "":
        opponent_history.append(prev_play)

    # Get current suggestions from your helper strategies
    suggestions = {
        'quincy': beat_Quincys(opponent_history),
        'mrugesh': beat_Mrugesh(my_history),
        'kris': beat_Kris(my_history),
        'abbey': beat_Abbeys(my_history),
    }

    # Pick expert with highest weight; prefer 'quincy' on exact tie (solid opener)
    best_expert = max(state['weights'], key=lambda k: (state['weights'][k], k == 'quincy'))
    guess = suggestions[best_expert]

    # Save suggestions for next round weight update
    state['last_suggestions'] = suggestions

    return guess


def player(prev_play, opponent_history=[], my_history=[], state={
    'weights': {'quincy': 0, 'mrugesh': 0, 'kris': 0, 'abbey': 0},
    'last_suggestions': None,
}):
    # Start of a new game: clear histories and reset weights
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        state['weights'] = {'quincy': 0, 'mrugesh': 0, 'kris': 0, 'abbey': 0}
        state['last_suggestions'] = None
    
    # pick a strategy based on working 
    guess = pick_strategy(prev_play, opponent_history, my_history, state)
    my_history.append(guess)
    return guess
