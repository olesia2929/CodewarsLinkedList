def loop_size(node):
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    loop_length = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        loop_length += 1
    return loop_length