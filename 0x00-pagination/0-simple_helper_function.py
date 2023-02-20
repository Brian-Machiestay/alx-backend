#!/usr/bin/env python3
""" A simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """compute the page number and return the start page
    """
    start_ind = (page - 1) * page_size
    end_ind = start_ind + page_size
    return ((start_ind, end_ind))
