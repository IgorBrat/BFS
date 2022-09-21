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
            ("up", (row + 1, column)),
            ("down", (row - 1, column)),
            ("left", (row, column - 1)),
            ("right", (row, column + 1)),
        ]
        for direction, (row, column) in actions:
            if 0 <= row < self.height and 0 <= column < self.width and not self.maze[row][column]:
                res.append((direction, (row, column)))
        return res

    def print(self):
        for row in self.maze:
            for el in row:
                print(el, end=" ")
            print()
