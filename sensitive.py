#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Assignment 3, Problem 1: Controlling the Maximum Flow

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
from src.sensitive_data import data  # noqa
from src.graph import Graph  # noqa
# If your solution needs a queue, then you can use this one:
from collections import deque  # noqa
# If you need to log information during tests, execution, or both,
# then you can use this library:
# Basic example:
#   logger = logging.getLogger('put name here')
#   a = 5
#   logger.debug(f"a = {a}")
import logging  # noqa

__all__ = ['sensitive']


def sensitive(G: Graph, s: str, t: str) -> Tuple[str, str]:
    """
    Pre:
    Post:
    Ex:   sensitive(g1, 'a', 'f') = ('b', 'd')
    """
    return None, None


class SensitiveTest(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """
    logger = logging.getLogger('SensitiveTest')
    data = data
    sensitive = sensitive

    def assertTypeSensitive(self, t: Any) -> None:
        self.assertEqual(type(t), tuple)
        self.assertEqual(len(t), 2)
        u, v = t
        if u is not None:
            self.assertEqual(type(u), str)
        if v is not None:
            self.assertEqual(type(v), str)

    def test_sensitive(self) -> None:
        """
        passing is not a guarantee of correctness.
        """
        for i, instance in enumerate(SensitiveTest.data):
            with self.subTest(instance=i):
                graph = instance['digraph'].copy()
                t = SensitiveTest.sensitive(graph, instance["source"],
                                            instance["sink"])

                self.assertTypeSensitive(t)
                u, v = t
                if len(instance["sensitive_edges"]) == 0:
                    self.assertEqual((u, v), (None, None))
                    continue

                self.assertIn(u, graph, f"Node '{u}' not in graph.")
                self.assertIn(v, graph, f"Node '{v}' not in graph.")
                self.assertIn((u, v), graph, f"Edge ({u}, {v}) not in graph.")
                self.assertIn((u, v), instance["sensitive_edges"])


if __name__ == "__main__":
    # Set logging config to show debug messages:
    logging.basicConfig(level=logging.DEBUG)
    # run unit tests (failfast=True stops testing after the first failed test):
    unittest.main(failfast=True)
