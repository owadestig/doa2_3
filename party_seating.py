#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Assignment 3, Problem 2: Party Seating

Team Number:
Student Names:
'''

'''
Copyright: justin.pearson@it.uu.se and his teaching assistants, 2022.

This file is part of course 1DL231 at Uppsala University, Sweden.

Permission is hereby granted only to the registered students of that
course to use this file, for a homework assignment.

The copyright notice and permission notice above shall be included in
all copies and extensions of this file, and those are not allowed to
appear publicly on the internet, both during a course instance and
forever after.
'''
from typing import *  # noqa
import unittest  # noqa
import math  # noqa
from src.party_seating_data import data  # noqa
# If your solution needs a queue, then you can use this one:
from collections import deque  # noqa
# If you need to log information during tests, execution, or both,
# then you can use this library:
# Basic example:
#   logger = logging.getLogger('put name here')
#   a = 5
#   logger.debug(f"a = {a}")
import logging  # noqa

__all__ = ['party']


def party(known: List[Set[int]]) -> Tuple[bool, Set[int], Set[int]]:
    """
    Pre:
    Post:
    Ex:   party([{1, 2}, {0}, {0}]) = True, {0}, {1, 2}
    """
    ## O(|known|)
    colors = [-1]*len(known)
    
    queue = []
    ## Loop through all guests

    ## O(|known|)
    for i in range(len(known)):
        ## If unnasigned
        if  colors[i] == -1:
            ## Assign color 0
            queue.append([i, 0])
            colors[i] = 0

            while len(queue) != 0:
                guest_and_color = queue[0]
                queue.pop(0)
                guest = guest_and_color[0]
                guest_color = guest_and_color[1]
                ## Traversing neighbours of guest

                ## O(l)
                for j in known[guest]:
                    ## If neighbour already colored with parents color
                    if colors[j] == guest_color:
                        return False, set(), set()
                    ## If uncolored
                    if colors[j] == -1:
                        if guest_color == 0:
                            colors[j] = 1
                        else:
                            colors[j] = 0
                        queue.append([j, colors[j]])

    table_1 = set()
    table_2 = set()

    #O(|known|)
    for i in range(len(known)):
        if colors[i] == 0:
            table_1.add(i)
        if colors[i] == 1:
            table_2.add(i)

    return True, table_1, table_2


class PartySeatingTest(unittest.TestCase):
    """
    Test suite for party seating problem
    """
    logger = logging.getLogger('PartySeatingTest')
    data = data
    party = party

    def assertTypeParty(self, t: Any) -> None:
        self.assertEqual(type(t), tuple)
        self.assertEqual(len(t), 3)
        success, A, B = t
        self.assertEqual(type(success), bool)
        self.assertEqual(type(A), set)
        self.assertEqual(type(B), set)
        for a in A:
            self.assertEqual(type(a), int)
        for b in B:
            self.assertEqual(type(b), int)

    def known_test(self, known: List[Set[int]], A: Set[int],
                   B: Set[int]) -> None:
        self.assertEqual(len(A) + len(B), len(known),
                         f"wrong number of guests: excepted {len(known)} "
                         f"guests, tables hold {len(A)} and {len(B)} guests "
                         "respectively")
        for g in range(len(known)):
            self.assertTrue(g in A or g in B, f"Guest {g} not seated anywhere")

        for a1, a2 in ((a1, a2) for a2 in A for a1 in A):
            self.assertNotIn(a2, known[a1],
                             f"Guests {a1} and {a2} seated together, and "
                             "know each other")

        for b1, b2 in ((b1, b2) for b2 in B for b1 in B):
            self.assertNotIn(b2, known[b1],
                             f"Guests {b1} and {b2} seated together, and "
                             "know each other")

    def test_party(self) -> None:
        """
        passing is not a guarantee of correctness.
        """
        for i, instance in enumerate(PartySeatingTest.data):
            with self.subTest(instance=i):
                known = instance["known"]
                expected = instance["expected"]

                t = PartySeatingTest.party(known)
                self.assertTypeParty(t)
                success, A, B = t

                if not expected:
                    self.assertFalse(success)
                    self.assertEqual(A, set())
                    self.assertEqual(B, set())
                else:
                    self.known_test(known, A, B)


if __name__ == '__main__':
    # Set logging config to show debug messages:
    logging.basicConfig(level=logging.DEBUG)
    # run unit tests (failfast=True stops testing after the first failed test):
    unittest.main(failfast=True)
