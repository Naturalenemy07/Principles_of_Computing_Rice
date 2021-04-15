import math

# Homework 4
def make_enum(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    # I still dont understand this function
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

def make_perm(outcomes, length):
    """
    
    """
    enumerations = make_enum(outcomes, length)
    permutations = []
    for enum in enumerations:
        if len(set(enum)) == len(enum):
            permutations.append(enum)
    return permutations

# Question 1
def q1():
    """
    Coinflips that generate set of 5 length
    """
    # number of different sides and length
    length = 5
    sid = 2

    # first set can be 2, next 2, next 2 and so on for length 5 or 2 ** 5
    tot = sid ** length
    print("Question 1: {}".format(tot))

# Question 2
# Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4) is rolled twice.  
# What is the expected value of the product of the two die rolls? Enter the answer as a floating point number below.

def q2():
    """
    Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4) is rolled twice.  
    What is the expected value of the product of the two die rolls? Enter the answer as a floating point number below.
    """
    def prod_lists_avg(list_list):
        """
        input::list_list: a iterable containing a set/list/tuple of enumerations
        output: returns the average of the products of input enumerations
        """
        list_of_products = []
        for lis in list_list:
            product = 1
            for ind in lis:
                product *= ind
            list_of_products.append(product)

        running = 0.0
        for prod in list_of_products:
            running += prod
        return running / len(list_of_products)


    # set constants ()
    sides = 4
    die_sides = range(1, sides + 1)
    rolls = 2

    # first make the list of lists of all possible enumerations
    poss_enum = make_enum(die_sides, rolls)

    # next get the product  abd averageof all enumerations
    print("Question 2: {}".format(prod_lists_avg(poss_enum)))


# Question 3
def q3():
    """
    Given a trial in which a decimal digit is selected from a list(0 - 9) with equal prob of 0.1.  Consider a 5-digit
    string created by a sequence of such trials(0s and repeated digits allowed). What is the probability that this
    5-string digit consists of five consecutive digits in ascending or descending order? 
    """
    # first compute the number of enumerations that match the required setting
    select_list = [0,1,2,3,4,5,6,7,8,9]
    
    counter = 0
    LENGTH = 4
    matched_enum = 1
    
    for i in range(len(select_list)):
        if i+LENGTH in select_list:
            counter += 1

    # because counter starts at zero we add 1 to it, and then multiply by 2 for acsending and descending
    consecutive_strings = (counter) * 2
    
    total_enum = make_enum(select_list, LENGTH + 1)
    prob_consec_string = float(consecutive_strings) / len(total_enum)

    print("Question 3: {}".format(prob_consec_string))
    
def q4():
    """
    Same as Question 3 but it is a permutation of digits instead of a combination (no repeated digits)
    """
    select_list = [0,1,2,3,4,5,6,7,8,9]
    
    counter = 0
    LENGTH = 4
    matched_enum = 1
    
    for i in range(len(select_list)):
        if i+LENGTH in select_list:
            counter += 1

    # Multiply by 2 for acsending and descending
    consecutive_strings = (counter) * 2
    
    total_perm = make_perm(select_list, LENGTH + 1)
    prob_consec_string = float(consecutive_strings) / len(total_perm)
    
    print("Question 4: {}".format(prob_consec_string))
    
def q5():
    """
    Write your own get all enumerations and permutations algorithm
    """
    """
    Function to generate permutations of outcomes
    Repetition of outcomes not allowed
    """

    def gen_permutations(outcomes, length):
        """
        Iterative function that generates set of permutations of
        outcomes of length num_trials
        No repeated outcomes allowed
        """
        enumerations = set([()])

        for dummy_idx in range(length):
            temp = set()
            for seq in enumerations:
                for item in outcomes:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
            enumerations = temp
        
        permutations = []
        for enum in enumerations:
            if len(set(enum)) == len(enum):
                permutations.append(enum)
        return permutations

    outcome = set(["a", "b", "c", "d", "e", "f"])
    
    permutations = gen_permutations(outcome, 4)
    permutation_list = list(permutations)
    permutation_list.sort()
    print("Question 5: {}".format(permutation_list[100]))

def q6():
    pass

def q7():
    """
    How many distinct subsets are in a set of length n, order isn't important...meaning (1,5) = (5,1)
    will trouble shoot later
    """
    test_set = [1, 2, 7]
    
    total_sets = []
    for index_length in range(1, len(test_set) + 1):
        total_sets.append(set(make_perm(test_set, index_length)))
    # sort, then append to new set
    sorte = []
    for ls in total_sets:
        for iter in ls:
            sorte.append(list(iter).sort())
    print("Question 7: 2^n")
    
def q8():
    """
    Combination: probability of being dealt 5 card hands of all the same suit
    """
    tot_cards = 52
    num_cards = 5
    cards_in_suit = 13
    
    prob_suit = 1.0000
    for i in range(0, num_cards):
        prob_suit *= (cards_in_suit - i) / (tot_cards - i)
    
    print("Qustion 8: {}".format(prob_suit))
    
def q9():
    """
    Iterative program to print out Pascal's triangle, I think the equation is m! /((m-n)!n!) - test it out and see if it matches
    """

    TRIANGLE_HEIGHT = 10

    def next_line(current_line):
        """
        Given a line in Pascal's triangle, generate the following line
        """

        ans = [1]

        for idx in range(len(current_line) - 1):
            ans.append(current_line[idx] + current_line[idx + 1])

        ans.append(1)

        return ans

    def run_example():
        # code to print out Pascal's triangle
        pascal_line = [1]	# row zero
        print(pascal_line)

        for dummy_idx in range(TRIANGLE_HEIGHT - 1):
            pascal_line = next_line(pascal_line)
            print(pascal_line)

    # this program tests the pascal triangle numbers     
    run_example()
    for m in range(0, TRIANGLE_HEIGHT):
        line = []
        for n in range(0, m + 1):
            line.append(str(int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n)))))
        print('  '.join(line))
        
TEST_CASES = [[0,1,1,1,1,10,8],[0,0,0,0,0,0,0,0],[0,10,10,10,10,10,1],[0,1,2,3,4,5,6,7,8,9,10],[0,10,9,8,7,6,5,4,3,2,1]]
    
#q1()
#q2()
#q3()
#q4()
#q5()
#q6()
#q7()
#q8()
#q9()
