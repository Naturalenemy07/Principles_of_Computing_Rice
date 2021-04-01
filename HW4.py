import math

## Homework 4

# # Question 1
# # Coinflips that generate set of 5 length

# # number of different sides and length
# length = 5
# sid = 2

# # first set can be 2, next 2, next 2 and so on for length 5 or 2 ** 5
# tot = sid ** length
# print(tot)

#Question 2
# Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4) is rolled twice.  
# What is the expected value of the product of the two die rolls? Enter the answer as a floating point number below.

def make_enum(choices, length): # need to change this, only works with two rolls and uses set name twice.
    set = []
    setofsets = []
    for indone in range(1, choices + 1):
        for indtwo in range(1, choices + 1):
            set = [indone, indtwo]
            setofsets.append(set)
    print(setofsets)
    return setofsets

def prod_lists(list_list):
    for lis in list_list:
        num = 1
        for ind in lis:
            num *= ind
        print(num)
        
# set constants
die_sides = 4
rolls = 1

# first make the list of lists of all possible enumerations
total_enum = die_sides ** rolls
poss_enum = make_enum(die_sides, rolls)
# added a small check to make sure enumerations are correct
if len(poss_enum) is not total_enum:
    print("Error: Enumerations are not correct")

# next get the product of all enumerations
prod_enum = prod_lists(poss_enum)

# lastly take the average of all the enumerations
