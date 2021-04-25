"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    # set score variables
    temp_max_score = 0
    running_max_score = 0
    
    # iterate through hand
    for numb in hand:
        # add all equal numbers
        for numb_iter in hand:
            if numb_iter is numb:
                running_max_score += numb_iter
        # compare previous high score with current num
        if running_max_score > temp_max_score:
            temp_max_score = running_max_score
        running_max_score = 0
    return temp_max_score
        


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # generate all sequences of dice being rolled
    rolled_dice_enum = gen_all_sequences(list(range(1, num_die_sides + 1)), num_free_dice)
    
    # join tuples to create a list of all possible held and rerolled dice
    total_dice = [held_dice + seq for seq in rolled_dice_enum]
    
    # calculate the expected value (score() of every roll / lenth of rolled dice enum)
    total_sum = sum([score(seq) for seq in total_dice])
    return float(total_sum)/len(total_dice)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = [()]
    for die in hand:
        for sub in all_holds:
            all_holds = all_holds + [tuple(sub) + (die,)]
        
    return set(all_holds)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """    
    # generate a set of all holds
    all_holds = gen_all_holds(hand)
    
    # generate the highest score/hold, store running highest
    highest_score = 0.0
    highest_hold = ()
    for hold in all_holds:
        print(hold)
        num_free_dice = len(hand) - len(hold)
        temp_score = float(expected_value(hold, num_die_sides, num_free_dice))
        if temp_score > highest_score:
            highest_score = temp_score
            highest_hold = hold
    
    return (highest_score, highest_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (2, 4, 2, 2, 3)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)
    
    
run_example()
#print(strategy((1,), 6))






