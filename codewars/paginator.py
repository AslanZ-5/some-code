#PaginationHelper
class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page

    def split(self):
        arr = self.collection
        arrs = []
        while len(arr) > self.item_per_page:
            pice = arr[:self.item_per_page]
            arrs.append(pice)
            arr = arr[self.item_per_page:]
        arrs.append(arr)
        return arrs


    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

        # returns the number of pages

    def page_count(self):
        import math
        return math.ceil(len(self.collection) / self.item_per_page)

        # returns the number of items on the current page. page_index is zero based
        # this method should return -1 for page_index values that are out of range

    def page_item_count(self, page_index):

        if self.split()[page_index]:
            return len(self.split()[page_index])
        else:
            return -1

        ## determines what page an item is on. Zero based indexes.
        # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):
        pass


a = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(a.page_count())
print(a.page_item_count(1))


# def split(arr,item):
#
#     arrs = []
#     while len(arr) > item:
#         pice = arr[:item]
#         arrs.append(pice)
#         arr = arr[item:]
#     arrs.append(arr)
#     return arrs
# print(split(['a','b','c','d','e','f'], 4)[])