"This is a practice mini-project that uses Monte Carlo algorithm"

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 1000

def evaluate_position(num_item):
    """
    uses Monte Carlo simulation to compute a good move
    """
    def iter_play(items_after_init_move):
        '''
        plays a single game with random moves for both computer and simulated_player until game is over, true is a win for the computer
        '''
        if True:
            return 1
        else:
            return 0
    
    '''
    ....Pseudo code....
    for each possible moves (max is MAX_REMOVE):
        score = []
        dict_of_move_scores = {}
        num_items -= move

        iteration = 0
        while iteration < TRIALS:
            # this passes the num_items after initial move to iter_play and appends 1 if a win or 0 if a loss for computer
            score.append(iter_play(num_item))
        
        # for each possible move, the score is set as a value to the move key example-{1: 0.4, 2: 0.6, 3: 0.2}
        dict_of_move_scores[move] = win_percentage(score)

        # next the highest value is chosen, that key is then the move that is performed by the computer
    '''

    return 0

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break


play_game(12)

### I wrote some functions that will be helpful
# returns 1 if true, 0 if false
# in this case, 4/10 win
score = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]

def win_percentage(score):
    win_fraction = score.count(1) / float(len(score))
    return win_fraction


def make_dict(maxval):
    dict = {}
    for dummy_i in range(1, maxval + 1):
        dict[dummy_i] = 0
    return dict

win_fraction = make_dict(MAX_REMOVE)
print "blank win fraction dictionary:", win_fraction

