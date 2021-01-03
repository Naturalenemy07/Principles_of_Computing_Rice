"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# This gives a 90% chance of selecting a 2 and a 10% chance of selecting a 4
WEIGHTED_NUMB_LIST = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

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
    
    # for loop that appends all non zero numbers in line
    # to a new list.  This list will be modified and output.
    for index in line:
        if index != 0:
            non_zero_list.append(index)
    
    # now merge adjacent numbers from left to right if same.
    len_non_zero_list = len(non_zero_list)
    
    # we don't want to compare the last number in the list
    # because there is no number after it, so we subtract 1.
    for nz_index in range(0, len_non_zero_list - 1):
        if non_zero_list[nz_index] == non_zero_list[nz_index + 1]:
            non_zero_list[nz_index] = non_zero_list[nz_index] * 2
            non_zero_list[nz_index + 1] = 0
    
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

    # finally, need to append zeros to non_zero_list so that it
    # is the same length as the input list
    len_mod_non_zero_list = len(non_zero_list)
    list_diff = len_list - len_mod_non_zero_list
    for dummy_num in range(0, list_diff):
        non_zero_list.append(0)
    return non_zero_list

class TwentyFortyEight:
    """
    Class to run the gameogic.
    """
    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid_dict = {}
        
        # initilize the initial tile for move function
        self._up_tiles = []
        self._down_tiles = []
        self._left_tiles = []
        self._right_tiles = []
        
        # logic for initial rows
        for dummy_tile in range(0, TwentyFortyEight.get_grid_width(self)):
            # logic for the up and down rows
            self._up_tiles.append((0, dummy_tile))
            self._down_tiles.append((TwentyFortyEight.get_grid_height(self) - 1, dummy_tile))
        for dummy_tile in range(0, TwentyFortyEight.get_grid_height(self)):
            # logic for the left and right rows
            self._left_tiles.append((dummy_tile, 0))
            self._right_tiles.append((dummy_tile, TwentyFortyEight.get_grid_width(self) - 1))
        
        # Store all initial tiles in a dictionary where direction of movement is keys
        self.initial_movement_tiles = {UP: self._up_tiles,
                                       DOWN: self._down_tiles,
                                       LEFT: self._left_tiles,
                                       RIGHT: self._right_tiles}
        
        # Initilize a new grid by calling reset
        TwentyFortyEight.reset(self)
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """        
        # First iterate through the height and width, adding that index to 
        # the self.grid_dict as a tuple and setting the value to zero
        for dummy_i in range(TwentyFortyEight.get_grid_width(self)):
            for dummy_j in range(TwentyFortyEight.get_grid_height(self)):
                #### remember to call method for setting numbers when created
                TwentyFortyEight.set_tile(self,dummy_j, dummy_i, 0)
        
        # Change two random tiles (if value is zero) to two or four
        counter = 0
        while counter < 2:
            if TwentyFortyEight.new_tile(self) is True:
                counter += 1

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # First make an empty string
        col_str = ""
        
        #need to make a column that contains the indexes of widthth
        dummy_col = range(0,TwentyFortyEight.get_grid_width(self))
        
        # for loop will set the first row values using dummy column
        # as the col_str, when complete with the row, 
        # it prints a new line using \n,
        # next, it repeats this for every row
        # finally it returns the entire string as a simple grid of numbers
        for dummy_i in range(TwentyFortyEight.get_grid_height(self)):
            for dummy_j in dummy_col:
                col_str += str(TwentyFortyEight.get_tile(self,dummy_i, dummy_j)) + " "
            col_str += "\n"
        return col_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

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
        # Function that randomly selects an index
        def rand_index_select():
            """
            This function randomly selects a tile within the gid
            """
            rand_height = random.randint(0,TwentyFortyEight.get_grid_height(self) - 1)
            rand_width = random.randint(0,TwentyFortyEight.get_grid_width(self) - 1)
            rand_index = (rand_height, rand_width)
            return rand_index
        
        # If the value of that index (key in dictionary) is 0,
        # change the value to two.  Call random index first.
        # Uses constant WEIGHTED_NUMB_LIST to ensure correct percentage
        rand_index_tile = rand_index_select()
        if self._grid_dict.get(rand_index_tile) == 0:
            self._grid_dict[rand_index_tile] = random.choice(WEIGHTED_NUMB_LIST)
            return True

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid_dict[(row, col)] = value
        return

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid_dict[(row, col)]


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
#print TwentyFortyEight(4, 4)

