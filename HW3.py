"""
HW 3 of Principles of Computing
Rice University
Coursera
"""

import random

## Question 2

total_cards = 52.0
cards_per_deck = 13.0

prob_specific_deck = cards_per_deck / total_cards
print "Question 2:", prob_specific_deck

## Question 3
# Consider a trial with 36 possible outcomes where each outcome has equal probability.  
# How many outcomes correspond to an event that has probability 1/9?
p_one = 1/36.0
t_outcomes = 36
tp_outcome = 1/9.0
p_event = 0
itern = 0

while p_event <= tp_outcome - p_one:
    p_event += p_one
    itern += 1

print "Question 3:", itern

## Question 4
# 6 sided single die 
#for i in range(100):
    #print random.randrange(1, 7) # yes
    #print random.randrange(6) # no
    #print random.randrange(6) + 1 # yes
    
## Question 5, They said rank but the available answers only work if they mean SUIT
p_first = 4.0/52
p_second = 3.0/51
sum_prob = p_first + p_second

print "probability of drawing two same suited cards:",sum_prob

## Question 6: Expected value
# mean GPA of class if 30% have a 4.0, 40% have a 3.0, 20% have a 2.0, and 10% have a 1.0

percentage = [0.3, 0.4, 0.2, 0.1]
gpa = [4.0, 3.0, 2.0, 1.0]

gpa_breakdown = []

for index in range(0, len(percentage)):
    gpa_breakdown.append(percentage[index] * gpa[index])

mean_gpa = 0

for gpa_index in gpa_breakdown:
    mean_gpa += gpa_index

print "Question 6:", mean_gpa

## Question 7: 
# even vs odd in 6 sided die, lose if odd, win if even
num_even = 3
num_odd = 3
p_each = 1.0 / 6

p_even = num_even * p_each
p_odd = num_odd * p_each

if p_even == p_odd:
    print "Question 7: expected winnings are zero, probability of even or odd number is the same"
elif p_even > p_odd:
    print "Question 7: expected winnings are negative"
elif p_even < p_odd:
    print "Question 7: expected winnings are positive"

## Question 8: what is the expected value of trial(n) below: assume n is a positive integer - enter as math expression in n:

def trial(n):
    val = random.randrange(n)
    return val

# the arithmetric sum from 0 to k has a value of 0.5 * k * (k + 1). 
# expected value is the sum of the a single outcome * the probability of that outcome.
# the probability of a single outcome is:

n = 10 # lets do 10 for example
p_single_outcome = 1.0 / n

# Expected value is the arithmetric sum * probability of individual outcome because of uniform distribution
a_sum = 0.5 * n * (n + 1)
exp_value = a_sum / n

## Question 9: Monte Carlo Simulations
# A unit circle surrounded by a square.  The function only returns points that are in the unit circle, each point in the square
# has an equal chance of being selected.
""" 
Program that computes mystery number
"""


import math
import random

def inside_unit_circle(point):
    """
    Compute distance of point from origin
    """
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance < 1
                                                 

def estimate_mystery(num_trials):
    """
    Main function
    """
    num_inside = 0
    
    for dumm_idx in range(num_trials):
        new_point = [2 * random.random() - 1, 2 * random.random() - 1]
        if inside_unit_circle(new_point):
            num_inside += 1
    
    return float(num_inside) / num_trials

print estimate_mystery(10000)

# the return value of estimate_mystery can be thought of as the area of the unit circle / area of the square surrounding unit cicle
#  or pi() / 4

## Question 10:

import poc_simpletest

def run_suite(format_func):
    
    # Create List of items
    LIST = [0005, 0050, 0061, 0120, 0560, 0600, 1232, 1325, 4567, 5999]
    result = ["0:00.5", "0:05.0", "0:06.1", "0:12.0", "0:56.0", "1:00.0", "2:03.2", "2:12.5", "7:36.7", "9:59.9"]
    
    # Create suite
    suite = poc_simpletest.TestSuite()

    # Initiate test
    for i in range(0, len(LIST)):
        suite.run_test(format_func(LIST[i]), result[i], "Test" + str(i) + ": ")
