class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None  
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
def move_node(source, dest):
    if source is None:
        raise ValueError
    new_node = source
    source = source.next
    new_node.next = dest
    dest = new_node
    return Context(source, dest)
