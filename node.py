from __future__ import annotations


class Node:
    def __init__(self, position: tuple, parent: Node, step: str):  # Should think about using enum
        self.position = position
        self.parent = parent
        self.step = step
