import os.path
from typing import List

import xmltodict

from .titles import ALL_TITLES
from .typing import Book


class Manga109:
    def __init__(self, root: str, titles: List[str] = ALL_TITLES):
        """
        Args:
            root (str): Path to the root directory.
            titles (List[str], optional): List of titles to load. Defaults to ALL_TITLES.
        """
        self._root = root
        self.books = self._read_books(root, titles)

    @staticmethod
    def _read_books(root: str, titles: List[str]) -> List[Book]:
        books: List[Book] = []

        for title in titles:
            with open(os.path.join(root, "annotations", f"{title}.xml")) as f:
                content = f.read()

            d = xmltodict.parse(content)
            book = Book.from_dict(d["book"], os.path.join(root, "images", title))
            books.append(book)
        return books
