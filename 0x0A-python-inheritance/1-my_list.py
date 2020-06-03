#!/usr/bin/python3
"""0x0A - 1 - My list"""


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
        print(sorted(self))
