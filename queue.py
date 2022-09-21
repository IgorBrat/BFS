from node import Node


class Queue:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def remove(self):
        if len(self.frontier) == 0:
            raise IndexError("Frontier is empty")
        else:
            elem_to_remove = self.frontier[0]
            self.frontier = self.frontier[1:]
            return elem_to_remove
