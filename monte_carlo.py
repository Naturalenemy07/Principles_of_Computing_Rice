"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
# This will print the board in the console line using the provided TTTBoard class as providedpass
def empty_scores(board):
    """
    Builds a board of scores with matching dimensions for board in play
    Returns an empty board
    """
    # Get dimensions of the board
    dim = board.get_dim()
    
    # Set row to empty list, set scores to another empty list
    row = []
    scores = []
    
    # Build the row of zero scores, add these rows to the scores list
    for dummy_row_index in range(dim):
        row.append(0)
    
    for dummy_row in range(dim):
        scores.append(row)
        
    return scores

def mc_trial(board, player):
    """
    Takes current board and the next player to move, makes random moves until game is finished
    """
    # randomly selects a row and column index and places the playerX or playerO in that
    # square if that square is empty, it does this until there is a winner
    # prints the board for testing purposes, returns nothing
    
    # get dimensions of the board
    dim = board.get_dim()
    
    # while board has no winner
    while board.check_win() is None:
        
        # set index for row and column within dimensions of board
        row = random.randrange(0, dim)
        col = random.randrange(0, dim)
        
        # if the (row, col) index is an empty square, set current player move at that square
        if (row, col) in board.get_empty_squares():
            board.move(row, col, player)
            
            # sets the next player
            player = provided.switch_player(player)
            
            # prints the board after each move
            print board
            
    return 
        

def mc_update_scores(scores, board, player):
    """
    takes a grid of scores, board of a completed game, and which player the machine is, 
    it scores the completed board and update scores grid
    """
    return "poop"

def get_best_move(board, scores):
    """
    takes the current board(must contain empty squares) and the grid of scores,
    finds maximum score and returns the one of them randomly
    """
    if len(board.get_empty_squares) == 0:
        print "Error: There are no more moves."
        return
    
    
def mc_move(board, player, trials):
    """
    takes the current board, which player machine is, and number of trials to run.
    Uses monte carlo simulation to return move for machine player as a tuple
    """    
    # monte carlo method
    for dummy_trial in range(0, trials):
        
        # started with a score of all zeros
        scores_grid = empty_scores(board)
        
        # play a random game until completion
        mc_trial(board, player)
        
        # score the completed game, set to a new running total, set to empty if first round 
        if dummy_trial is 0:
            scores_total = scores_grid
            scores_total = mc_update_scores(scores_total, board, player)
        else:
            scores_total = mc_update_scores(scores_total, board, player)

    # test scoring algorithm after a completed game
    print scores_total
        
    # get the best move
    #get_best_move(board, scores_total)
       

# test the mc_trial function
board = provided.TTTBoard(3)
# empty_scores(board) # test building scores board
# mc_trial(board, provided.PLAYERX)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)





