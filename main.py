from detector_maze import DetectorMaze


def main():
    print("Maze 0:")
    maze = DetectorMaze("resources/input.txt")
    maze.print_maze()
    print()
    maze.find_shortest_path("resources/output.txt")
    print()

    # print("Maze 1:")
    # maze1 = DetectorMaze("resources/input1.txt")
    # maze1.print_maze()
    # print()
    # maze1.find_shortest_path("resources/output1.txt")
    # print()
    #
    # print("Maze 2:")
    # maze2 = DetectorMaze("resources/input2.txt")
    # maze2.print_maze()
    # print()
    # maze2.find_shortest_path("resources/output2.txt")
    # print()
    #
    # print("Maze 3:")
    # maze3 = DetectorMaze("resources/input3.txt")
    # maze3.print_maze()
    # print()
    # maze3.find_shortest_path("resources/output3.txt")
    # print()


if __name__ == '__main__':
    main()
