class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    first_head = head
    second_head = head.next if head else None
    first = first_head
    second = second_head
    while first and first.next and second and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next
    if first:
        first.next = None
    if second:
        second.next = None
    return Context(first_head, second_head)
