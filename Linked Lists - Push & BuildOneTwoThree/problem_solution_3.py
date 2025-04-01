class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    """
    pushes a new node to the head of the linked list.
    """
    if head is None:
        return Node(data)
    else:
        new_node = Node(data)
        new_node.next = head
        return new_node 
def build_one_two_three():
    """
    builds.
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head