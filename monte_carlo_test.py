"""
Testing for monte_carlo.py on CodeSkulptor.org
"""

import poc_simpletest

def run_suite(function):
    # create the testsuite object
    suite = poc_simpletest.TestSuite()
    
    # test board printing
    threeboard = "  |   |  \n---------\n  |   |  \n---------\n  |   |  "
    suite.run_test(function(3, reverse = False), threeboard, "Test 3x3:")
