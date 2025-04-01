# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
def linked_list_from_string(s):
    """
    convert a string representation of a linked list to a linked list.
    """
    data = s.split(' -> ')
    data.remove('None')
    node = None
    for i in reversed(data):
        node = Node(int(i), node)
    return node
