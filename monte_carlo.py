"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 200         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0 # Score for squares played by the other player
    
# Add your functions here.
# This will print the board in the console line using the provided TTTBoard class as providedpass
def empty_scores(board):
    """
    Builds a board of scores with matching dimensions for board in play
    Returns an empty board
    """
    # Get dimensions of the board
    dim = board.get_dim()

    # Set scores to empty list, will hold all other lists
    scores = []
    
    # Build the row of zero scores, add these rows to the scores list
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(0)
        scores.append(row)
        
    return scores

def mc_trial(test_board, player):
    """
    Takes current board and the next player to move, makes random moves until game is finished
    """
    # randomly selects a row and column index and places the playerX or playerO in that
    # square if that square is empty, it does this until there is a winner
    # prints the board for testing purposes, returns nothing
    
    # get dimensions of the board
    dim = test_board.get_dim()
    
    # while board has no winner
    while test_board.check_win() is None:
        
        # set index for row and column within dimensions of board
        row = random.randrange(0, dim)
        col = random.randrange(0, dim)
        
        # if the (row, col) index is an empty square, set current player move at that square
        if (row, col) in test_board.get_empty_squares():
            test_board.move(row, col, player)
            
            # sets the next player
            player = provided.switch_player(player)
            
    # prints the board for testing purposes            
    return test_board
        

def mc_update_scores(scores, test_board, player):
    """
    takes a grid of scores, board of a completed game, and which player the machine is, 
    it scores the completed board and update scores grid
    """
    # get dimensions of the board
    dim = test_board.get_dim()
    
    # sets winner to a variable using check_win(), 2 is "X", 3 is "O", 4 is "draw"
    winner = test_board.check_win()
    
    # if tied
    if winner is provided.DRAW:
        for i in range(dim):
            for j in range(dim):
                scores[i][j] = scores[i][j] + 0
    
    # if winner is player, add point for player, minus for other, zero for blank
    elif winner is player:
        for lis in range(dim):
            for element in range(dim):
                if test_board.square(lis, element) is provided.EMPTY:
                    scores[lis][element] = scores[lis][element] + 0
                elif test_board.square(lis, element) is player:                    
                    scores[lis][element] += SCORE_CURRENT
                else:
                    scores[lis][element] -= SCORE_OTHER                    
    
    # if winner is not the player
    elif winner is not player:
        for lis in range(dim):
            for element in range(dim):
                if test_board.square(lis, element) is provided.EMPTY:
                    scores[lis][element] = scores[lis][element] + 0
                elif test_board.square(lis, element) is player:                    
                    scores[lis][element] -= SCORE_CURRENT
                else:
                    scores[lis][element] += SCORE_OTHER 
    return scores
    
            

def get_best_move(board, scores):
    """
    takes the current board(must contain empty squares) and the grid of scores,
    finds maximum score and returns the one of them randomly
    """
    if len(board.get_empty_squares()) == 0:
        print "Error: There are no more moves."
        return
    else:
        # returns tuple of the highest score, random if tie
        empty_squares = board.get_empty_squares()   
        
        # create a list of all scores and list of empty positions
        empty_scores_list = []
        highest_score = 0
        for list_item in range(len(scores)):
            for ele_item in range(len(scores)):
                score_tuple = (list_item, ele_item)
                if score_tuple in empty_squares:
                    empty_scores_list.append(scores[list_item][ele_item])
        
        # build a dictionary with both location as key
        # and the score as value
        score_pos_dict = {}
        i = 0
        for score in empty_scores_list:
            score_pos_dict[score] = empty_squares[i]
            i += 1
    
        # get the highest score
        score_values = score_pos_dict.keys()
        score_values.sort(reverse = True)
        highest_score = score_values[0]
        
        # get the location of the highest value, returns key
        highest_score_index = score_pos_dict[highest_score]
        return highest_score_index
    
    
def mc_move(board, player, trials):
    """
    takes the current board, which player machine is, and number of trials to run.
    Uses monte carlo simulation to return move for machine player as a tuple
    """    
    # get dimensions
    dim = board.get_dim()
    
    # monte carlo method
    for dummy_trial in range(0, trials):
        
        # play a random game until completion, set to test board
        test_board = board.clone()
        mc_trial(test_board, player)
        
        # score the completed game, set to a new running total, set to empty if first round 
        if dummy_trial is 0:
            scores_total = mc_update_scores(empty_scores(board), test_board, player)
        elif dummy_trial > 0:
            scores_total = mc_update_scores(scores_total, test_board, player)
    
    # get the best move score, returns a tuple
    x = get_best_move(board, scores_total)
    print x
       

# test the mc_trial function
##board = provided.TTTBoard(3)
# empty_scores(board) # test building scores board
##mc_trial(board, provided.PLAYERX)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

