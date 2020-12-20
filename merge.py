"""
Merge function for 2048 game.
"""

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
