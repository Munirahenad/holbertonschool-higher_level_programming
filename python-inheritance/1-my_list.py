#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order (without modifying it)."""
        print(sorted(self))
