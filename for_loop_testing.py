num_list = [1,2,3]

# This is how I traditionally write a for loop, iterating through each item
# performing operation, then appending to the designated list
sq_num_list = []
for item in num_list:
    sq_num_list.append(item ** 2)
print("traditional for loop: {}".format(sq_num_list))

# This tests the ability to make a lined for loop
# since it is set to a named list, it will automatically append to that list, instead of making a new list each time
# prints of the num_list items squared
sq_num_list_line = [item ** 2 for item in num_list]
print("lined for loop: {}".format(sq_num_list_line))
