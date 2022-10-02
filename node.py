from __future__ import annotations


class Node:
    def __init__(self, position: tuple, parent: Node = None):  # Should think about using enum
        self.position = position
        self.parent = parent

    def __str__(self):
        return str(self.position)
