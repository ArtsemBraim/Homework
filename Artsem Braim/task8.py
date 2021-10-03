import math


class Pagination:

    def __init__(self, text, page_size):
        self._text = text
        self._page_size = page_size

    @property
    def page_count(self):
        return math.ceil(len(self._text) / self._page_size)

    @property
    def item_count(self):
        return len(self._text)

    def count_items_on_page(self, page):
        if page >= self.page_count:
            raise IndexError("Invalid index. Page is missing")
        elif page == self.page_count - 1:
            return self._page_size - (self._page_size * self.page_count - len(self._text))
        else:
            return self._page_size


if __name__ == "__main__":
    pages = Pagination('Your beautiful text', 5)
    print(pages.page_count)
    print(pages.item_count)
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    print(pages.count_items_on_page(4))
