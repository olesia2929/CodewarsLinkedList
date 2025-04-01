# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next
def stringify(node):
    """
    convert a linked list to a string representation.
    """
    temp_l = []
    result = ' -> '
    while node:
        temp_l.append(str(node.data))
        node = node.next
    temp_l.append('None')
    return result.join(temp_l)
