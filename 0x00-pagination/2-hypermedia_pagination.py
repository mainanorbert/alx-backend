#!/usr/bin/env python3
""" module for Simple helper function"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """function that implements simple helper function
    for pagination"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

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
        """implemting pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        total_page_size = math.ceil(len(dataset) / page_size)
        if page > total_page_size:
            return []
        start_idx, end_idx = index_range(page, page_size)
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Hypermedia pagination"""
        hyper_dict = {}
        total_page_size = math.ceil(len(self.dataset()) / page_size)
        if page >= total_page_size:
            next_page = None
        else:
            next_page = page + 1
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1
        data = self.get_page(page, page_size)
        hyper_dict['page_size'] = len(data)
        hyper_dict['page'] = page
        hyper_dict['data'] = data
        hyper_dict['next_page'] = next_page
        hyper_dict['prev_page'] = prev_page
        hyper_dict['total_pages'] = total_page_size
        return hyper_dict
