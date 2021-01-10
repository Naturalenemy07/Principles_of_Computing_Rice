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

for index in percentage:
    gpa_breakdown.append(percentage[index] * gpa[index])

mean_gpa = 0

for gpa_index in gpa_breakdown:
    mean_gpa += gpa_breakdown[gpa_index]

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

