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
    
q1()
q2()
q3()

