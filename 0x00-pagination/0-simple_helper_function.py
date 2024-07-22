#!/usr/bin/env python3
"""
index range module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns tuple of size two containing:
        start index and an end index corresponding to
        range of indexes to return in a list for those particular
        pagination parameters.
    """
    end: int = page * page_size
    start: int = end - page_size
    return (start, end)
