#!/usr/bin/env python3
""" module for Simple helper function"""


def index_range(page, page_size):
    """function that implements simple helper function
    for pagination"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
