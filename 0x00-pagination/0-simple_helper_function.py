#!/usr/bin/env python3
"""A function that takes two integer arguments
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for the
    given pagination parameters.

    Args:
        page (int): the number of the page
        page_size (int): the number of items per page

    Returns:
        tuple: start and end indexes of current page.
    """
    # calculate start index by subtracting 1 from the current page number
    # and then multiplying by the page size
    start_index = (page - 1) * page_size
    # calculate end index by adding the start index to the page size
    end_index = start_index + page_size
    # return the start and end indexes as a tuple
    return (start_index, end_index)
