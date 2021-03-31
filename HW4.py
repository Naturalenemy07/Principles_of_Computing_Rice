import math

## Homework 4

# Question 1
# Coinflips that generate set of 5 length

# number of different sides and length
length = 5
sid = 2

# first set can be 2, next 2, next 2 and so on for length 5 or 2 ** 5
tot = sid ** length
print(tot)
