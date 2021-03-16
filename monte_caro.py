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
    # get dimensions of the board
    dim = board.get_dim()
    
    # sets winner to a variable using check_win(), 2 is "X", 3 is "O", 4 is "draw"
    winner = board.check_win()
    
    # if tied
    if winner is 4:
        print "tie"
        for i in range(dim):
            for j in range(dim):
                scores[i][j] = scores[i][j] + 0
    
    # if winner is player
    elif winner is player:
        print "winner:", winner, "player:", player
        for list in board:
            for element in list:
                if board.square(i, j) is player:
                    print "square:",i, j, "board:", board.square(i, j),"player:", player
                    print scores[i][j]
                    scores[i][j] += 1
                    print scores[i][j]
                    
    
    # if winner is not the player
    elif winner is not player:
        print "winner:", winner, "player:", player
    
    return scores
    
            

def get_best_move(board, scores):
    """
    takes the current board(must contain empty squares) and the grid of scores,
    finds maximum score and returns the one of them randomly
    """
    if len(board.get_empty_squares) == 0:
        print "Error: There are no more moves."
        pass
    
    
def mc_move(board, player, trials):
    """
    takes the current board, which player machine is, and number of trials to run.
    Uses monte carlo simulation to return move for machine player as a tuple
    """    
    # get dimensions
    dim = board.get_dim()
    
    # monte carlo method
    for dummy_trial in range(0, trials):
        
        # play a random game until completion
        mc_trial(board, player)
        
        # score the completed game, set to a new running total, set to empty if first round 
        print "trial", dummy_trial
        if dummy_trial is 0:
            scores_total = mc_update_scores(empty_scores(board), board, player)
        elif dummy_trial > 0:
            scores_total = mc_update_scores(scores_total, board, player)
                    
        # test scoring algorithm after a completed game
        print scores_total
        
    # get the best move score
    # get_best_move(board, scores_total)
       

# test the mc_trial function
##board = provided.TTTBoard(4)
# empty_scores(board) # test building scores board
##mc_trial(board, provided.PLAYERX)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

