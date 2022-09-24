from detector_maze import DetectorMaze


def main():
    maze = DetectorMaze("input.txt", "")
    maze.print_maze()
    print(maze.bfs_last_column((0, 9)))
    maze.print_solution()


if __name__ == '__main__':
    main()
