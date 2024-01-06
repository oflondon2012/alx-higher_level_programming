#!/usr/bin/python3
"""Function to locked class."""


class LockedClass:
    """This class prevent user
    from instantiating new LockedClass attributes
    for anything only called 'first_name'.
    """

    __slots__ = ["first_name"]
