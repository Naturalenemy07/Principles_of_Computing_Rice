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
    def win_percentage(score):
        """
        calculates the win percentage of a list score; 1 is win , 0 is loss
        """
        win_fraction = score.count(1) / float(len(score))
        return win_fraction
    
    def iter_play(remaining):
        '''
        plays a single game with random moves for both computer and simulated_player until game is over, true is a win for the computer
        '''
        play = 0
    
        # while loop to play until game is done, switching between players
        # if play is an even number, then it is the "players" turn, 
        # if it is odd, it is the computer's turn
        while remaining > 0:
            turn = random.randrange(1, MAX_REMOVE + 1)
            if remaining - turn >= 0:
                # subtract the turn if a valid move
                remaining -= turn
                play += 1
        if remaining == 0:
            if play % 2 == 0:
                return 1
            else: 
                return 0
            print ""
    
    # Main logic of the evaluate_position() function
    # for loop will iterate through each possible initial move
    # and pass to iter_play for a certain number of trials
    # it calculates the percentage win and then selects the 
    # initial move with the highest win percentage
    # dict_move_scores stores the win percentage for each possible initial move
    dict_move_scores = {}
    
    # store original value
    original_num_input = num_item
    
    for move in range(1, MAX_REMOVE + 1):
        score = []
        # set num_item to original value for further iterations
        num_item = original_num_input
        num_item -= move
        
        iteration = 1
        while iteration <= TRIALS:
            # pass the number of items leftover after initial move to iter_play()
            # The while loop will play the game for a set amount of trials
            # The wins are 1, losses are 0
            score.append(iter_play(num_item))
            iteration += 1
        dict_move_scores[move] = win_percentage(score)
        
    # next the best move need to be chosen by selecting the highest winning move
    max_value = max(dict_move_scores.values())
    max_pos = dict_move_scores.values().index(max_value)
    best_move = dict_move_scores.keys()[max_pos]    
    return best_move
    
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

play_game(21)

# I am adding this comment to test
