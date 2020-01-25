"""
functions.py
A python package for analyzing some stuff other than playing modern warfare!

Handles the primary functions
"""

import os


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "This package is coolish!!!"
    if with_attribution:
        quote += "\n\t- Adapted from Sergentu Claudiu"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
