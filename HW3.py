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
    
## Question 5
p_first = 4.0/52
p_second = 3.0/51
sum_prob = p_first + p_second

print "probability of drawing two same ranked cards:",sum_prob
    
