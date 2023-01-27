#!/usr/bin/env python3
""" Simple pagination
"""

import csv
import math
from typing import List


def index_range(page, page_size) -> tuple:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        if self.dataset() is None:
            return []

        indexRange = index_range(page, page_size)
        return self.dataset()[indexRange[0]: indexRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dict containing info of the page.
        """
        data = self.get_page(page, page_size)
        DataSet = self.__dataset
        lenSet = len(DataSet) if DataSet else 0

        totalPages = math.ceil(lenSet / page_size) if DataSet else 0
        page_size = len(data) if data else 0

        prevPage = page - 1 if page > 1 else None
        nextPage = page + 1 if page < totalPages else None

        hyperMedia = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }

        return hyperMedia
