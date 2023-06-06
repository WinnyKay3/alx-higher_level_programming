#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevents user from instantiatin a new lockedClass attribute."""

    __slots__ = ["first_name"]

