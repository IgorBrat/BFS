from node import Node
from bfs.my_queue import Queue
from step import Step


class DetectorMaze:
    def __init__(self, input_file: str, output_file: str):
        with open(input_file) as file:
            maze = file.read().splitlines()
        self.height = len(maze)
        if max(len(line) for line in maze) != min(len(line) for line in maze):
            raise ValueError("Maze must be rectangular")
        self.width = max(len(line) for line in maze)
        self.maze = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(int(maze[i][j]))
            self.maze.append(row)
        self.__spread_detectors()
        self.path = []

    def __spread_detectors(self):
        #  Time complexity is O(n^2), should think on reducing it
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == 0:
                    if i != 0:
                        self.maze[i - 1][j] = -1
                        if j != 0:
                            self.maze[i - 1][j - 1] = -1
                            self.maze[i][j - 1] = -1
                        if j != self.width - 1:
                            self.maze[i - 1][j + 1] = -1
                            self.maze[i][j + 1] = -1
                    if i != self.height - 1:
                        self.maze[i + 1][j] = -1
                        if j != 0:
                            self.maze[i + 1][j - 1] = -1
                            self.maze[i][j - 1] = -1
                        if j != self.width - 1:
                            self.maze[i + 1][j + 1] = -1
                            self.maze[i][j + 1] = -1
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == -1:
                    self.maze[i][j] = 0

    def get_neighbours(self, position: tuple):
        row, column = position
        res = []
        actions = [
            (Step.UP, (row + 1, column)),
            (Step.DOWN, (row - 1, column)),
            (Step.LEFT, (row, column - 1)),
            (Step.RIGHT, (row, column + 1)),
        ]
        for step, (row, column) in actions:
            if 0 <= row < self.height and 0 <= column < self.width and self.maze[row][column]:
                res.append((step, (row, column)))
        return res

    def __get_len_of_path(self, node: Node):
        len_of_path = 0
        self.path.append(node.position)
        while node.parent is not None:
            len_of_path += 1
            node = node.parent
            self.path.append(node.position)
        return len_of_path

    def bfs_last_column(self, start: tuple):
        if start[0] not in range(self.height) or start[1] not in range(self.width):
            raise IndexError("Element is out of bonds of the maze")
        if self.maze[start[0]][start[1]] == 0:
            raise ValueError("Can`t start from detector field range")
        queue = Queue()
        explored = set()
        if start[1] == self.width - 1:
            self.path.append(start)
            return 0
        start = Node(start)
        queue.add(start)
        while True:
            if queue.is_empty():
                return -1
            node = queue.remove()
            if node.position[1] == self.width - 1:
                return self.__get_len_of_path(node)
            explored.add(node.position)
            for step, position in self.get_neighbours(node.position):
                if not queue.contains_element(position) and position not in explored:
                    queue.add(Node(position, node, step))

    def print_maze(self):
        for row in self.maze:
            for el in row:
                if el == 0:
                    print('\033[91m' + str(el) + '\033[0m', end=" ")
                else:
                    print(el, end=" ")
            print()

    def print_solution(self):
        for i in range(self.height):
            for j in range(self.width):
                el = self.maze[i][j]
                if (i, j) in self.path:
                    print('\033[92m' + str(el) + '\033[0m', end=" ")
                elif el == 0:
                    print('\033[91m' + str(el) + '\033[0m', end=" ")
                else:
                    print(el, end=" ")
            print()
