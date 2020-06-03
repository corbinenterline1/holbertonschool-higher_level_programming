#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """MyList class. Currently only contains public instance method
    print_sorted, which prints the sorted list.

    Args:
        list: parent to inherit from
        """
    def print_sorted(self):
        """Method to print list that has been sorted.

        Args:
            self: self
            """
        slisty = self[:]
        print(sorted(slisty))
