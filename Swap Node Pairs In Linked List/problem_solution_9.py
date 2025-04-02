class Node:
    def __init__(self, next=None):
        self.next = next
def swap_pairs(head):
    current = head
    prev = None
    while current and current.next:
        next_pair = current.next.next
        if prev:
            prev.next = current.next
        else:
            head = current.next
        current.next.next = current
        current.next = next_pair
        prev = current
        current = next_pair
    return head
