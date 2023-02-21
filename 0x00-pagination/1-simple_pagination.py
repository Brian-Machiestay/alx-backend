#!/usr/bin/env python3
""" A simple helper function"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """compute the page number and return the start page
    """
    start_ind = (page - 1) * page_size
    end_ind = start_ind + page_size
    return ((start_ind, end_ind))


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
        """return a page"""
        assert(type(page_size) is int)
        assert(type(page_size) is int)
        assert(page > 0)
        assert(page_size > 0)
        start_index, end_index = index_range(page, page_size)
        with open('Popular_Baby_Names.csv', newline='') as f:
            allData = csv.reader(f, delimiter='\n')
            pages = [[field for field in row[0].split(',')] for row in allData]
            pages.pop(0)
        if end_index > len(pages):
            return []
        return pages[start_index: end_index]
