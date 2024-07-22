#!/usr/bin/env python3
"""
index range module
"""
import csv
import math
from typing import Tuple, List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "baby_names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        indexes dataset within valid give range
        """

        if not isinstance(page, int) or \
            not isinstance(page_size, int) or \
                page <= 0 or page_size <= 0:
            assert False

        range_ = index_range(page, page_size)
        data = self.dataset()

        return data[range_[0]: range_[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        hypermedia pagination
        """

        if not isinstance(page, int) or \
            not isinstance(page_size, int) or \
                page <= 0 or page_size <= 0:
            assert False

        data = self.dataset()

        response = self.get_page(page, page_size)

        if len(response) != 0:
            total_pages = math.floor(len(data) / len(response))
        else:
            total_pages = 0

        media = {
            'page_size': len(response),
            'page': page,
            'data': response,
            'next_page': page + 1 if len(response) != 0 else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }

        return media
