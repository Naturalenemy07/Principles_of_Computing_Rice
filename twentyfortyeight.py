"""
Clone of 2048 game.
"""

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    non_zero_list = []
    len_list = len(line)
#    print "Input list"
#    print line
#    print ""
    
    # for loop that appends all non zero numbers in line
    # to a new list.  This list will be modified and output.
    for index in line:
        if index != 0:
            non_zero_list.append(index)
#    print "Original Non-zero list"
#    print non_zero_list
#    print ""
    
    # now merge adjacent numbers from left to right if same.
    len_non_zero_list = len(non_zero_list)
    
    # we don't want to compare the last number in the list
    # because there is no number after it, so we subtract 1.
    for nz_index in range(0, len_non_zero_list - 1):
        if non_zero_list[nz_index] == non_zero_list[nz_index + 1]:
            non_zero_list[nz_index] = non_zero_list[nz_index] * 2
            non_zero_list[nz_index + 1] = 0
#    print "Quasi-merged non-zero list"
#    print non_zero_list
#    print ""
    
    # Now, need to remove the zero's from modified list
    # need a placeholder list so don't modify list in loop.
    placeholder_list = []
    for nzq_index in range(0, len_non_zero_list):
        if non_zero_list[nzq_index] == 0:
            placeholder_list.append(nzq_index)
    
    # Next, go through placeholder list and popout the 
    # index from modified non_zero_list. needed step 
    # because we were popping a value out, and the step
    # corrects for that index
    step = 0
    for place_index in placeholder_list:
        non_zero_list.pop(place_index - step)
        step += 1
    
#    print "No zero modified non zero list"
#    print non_zero_list
#    print ""

    # finally, need to append zeros to non_zero_list so that it
    # is the same length as the input list
    len_mod_non_zero_list = len(non_zero_list)
    list_diff = len_list - len_mod_non_zero_list
    for dummy_num in range(0, list_diff):
        non_zero_list.append(0)
    
#    print "Final list"
    return non_zero_list

class TwentyFortyEight:
    """
    Class to run the gameogic.
    """
    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        
        # Initilize a new grid by calling reset
        TwentyFortyEight.reset(self)

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # First need to initialize a blank dictionary that stores 
        # grid index as keys and the value is the number
        grid_dict = {}
        
        # Next iterate through the height and width, adding that index to 
        # the grid_dict as a tuple and setting the value to zero
        for dummy_i in range(self.width):
            for dummy_j in range(self.height):
                grid_dict[(dummy_j, dummy_i)] = 0
                
        print grid_dict

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
TwentyFortyEight(2, 3)
