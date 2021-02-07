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

def mc_trial(board, player):
    """
    Takes current board and the next player to move, makes random moves until game is finished
    """
    #get dimensions of the board
    dim = board.get_dim()

    # randomly selects a row and column index and places the playerX or playerO in that
    # square if that square is empty, it does this until the board is full
    # returns a clone of the board

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
    pass

def get_best_move(board, scores):
    """
    takes the current board(must contain empty squares) and the grid of scores,
    finds maximum score and returns the one of them randomly
    """
    if len(board.get_empty_squares) == 0:
        print "Error: There are no more moves."
        return
    else:
        pass

def mc_move(board, player, trials):
    """
    takes the current board, which player machine is, and number of trials to run.
    Uses monte carlo simulation to return move for machine player as a tuple
    """
    # monte carlo
    for dummy_trial in range(0, trials):
        # start with scores of all 0, build grid with nest forloop
    	score_grid = []
    	dim = board.get_dim()
    	for x_int in range(0, dim):
        	x_grid = []
        	for y_int in range(0, dim):
            	x_grid.append(0)
        	score_grid.append(x_grid)
    	print score_grid
        
        # play a random game until completion
        mc_trial(board, player)
        # passes this board to be scored
        mc_update_scores(score_grid, board, player)


# test the mc_trial function
board = provided.TTTBoard(3)
mc_trial(board, provided.PLAYERX)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
