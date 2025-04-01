# from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def get_nth(node, index):
    """
    returns the nth node in the linked list.
    """
    if node is None:
        raise ValueError
    if index < 0:
        raise ValueError
    if index == 0:
        return node
    current = node
    count = 0
    while current is not None:
        if count == index:
            return current
        current = current.next
        count += 1
    raise ValueError