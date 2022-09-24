from node import Node
from bfs.my_queue import Queue


class DetectorMaze:
    def __init__(self, input_file: str):
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
        candidates = [
            (row + 1, column),
            (row - 1, column),
            (row, column - 1),
            (row, column + 1),
        ]
        for (row, column) in candidates:
            if 0 <= row < self.height and 0 <= column < self.width and self.maze[row][column]:
                res.append((row, column))
        return res

    def __get_path(self, node: Node):
        path = [node.position]
        while node.parent is not None:
            node = node.parent
            path.append(node.position)
        return path

    def bfs_last_column(self, start: tuple):
        if start[0] not in range(self.height) or start[1] not in range(self.width):
            raise IndexError("Element is out of bonds of the maze")
        if self.maze[start[0]][start[1]] == 0:
            raise ValueError("Can`t start from detector field range")
        queue = Queue()
        explored = set()
        if start[1] == self.width - 1:
            return 0, [start]
        start = Node(start)
        queue.add(start)
        while True:
            if queue.is_empty():
                return -1, None
            node = queue.remove()
            if node.position[1] == self.width - 1:
                path = self.__get_path(node)
                return len(path) - 1, path
            explored.add(node.position)
            for position in self.get_neighbours(node.position):
                if not queue.contains_element(position) and position not in explored:
                    queue.add(Node(position, node))

    def find_shortest_path(self, output_file: str):
        paths = []
        for i in range(self.height):
            if self.maze[i][0] == 1:
                curr_path_len, curr_path = self.bfs_last_column((i, 0))
                if curr_path_len == self.width:
                    self.print_solution(curr_path)
                    self.write_res_to_file(output_file, curr_path)
                    return
                elif curr_path_len != -1:
                    paths.append((i, curr_path))
        if len(paths) == 0:
            print("No path available")
            self.write_res_to_file(output_file, [])
        else:
            paths.sort(key=lambda el: len(el[1]))
            self.print_solution(paths[0][1])
            self.write_res_to_file(output_file, paths[0][1])

    def print_maze(self):
        for row in self.maze:
            for el in row:
                if el == 0:
                    print('\033[91m' + str(el) + '\033[0m', end=" ")
                else:
                    print(el, end=" ")
            print()

    def print_solution(self, curr_path):
        for i in range(self.height):
            for j in range(self.width):
                el = self.maze[i][j]
                if (i, j) in curr_path:
                    print('\033[92m' + str(el) + '\033[0m', end=" ")
                elif el == 0:
                    print('\033[91m' + str(el) + '\033[0m', end=" ")
                else:
                    print(el, end=" ")
            print()

    def write_res_to_file(self, output_file: str, path):
        with open(output_file, 'w') as file:
            for i in range(self.height):
                for j in range(self.width):
                    el = self.maze[i][j]
                    if (i, j) in path:
                        file.write(f"{el} ")
                    elif el == 0:
                        file.write("# ")
                    else:
                        file.write("_ ")
                file.write("\n")
            file.write("\nLength of the shortest path: " + str(len(path)-1))
