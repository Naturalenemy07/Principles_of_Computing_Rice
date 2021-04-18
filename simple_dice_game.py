"""
Analyzing a simple dice game, mini project to help with project
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits


def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    repeats = [seq.count(item) for item in seq]
    return max(repeats)


def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """
    TRIPLE = 200
    DOUBLE = 10
    
    all_rolls = gen_all_sequences([1, 2, 3, 4, 5, 6], 3)
    num_repeats = [max_repeats(roll) for roll in all_rolls]
    
    total_amount = 0.0
    for repeat in num_repeats:
        if repeat is 3:
            total_amount += TRIPLE
        elif repeat is 2:
            total_amount += DOUBLE
        else:
            pass
    return round(total_amount / len(all_rolls), 2)

def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print "All possible sequences of three dice are"
    print gen_all_sequences(outcomes, 3)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value()
    
run_test()

