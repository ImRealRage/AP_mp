def solve_maze_dfs(maze, start, end):
    def is_valid(x, y):

        # Check if the cell is within the maze boundaries and is not a wall
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

    def dfs(x, y, path, steps):
        # Mark the current cell as visited
        maze[x][y] = 2  # Mark it as visited
        steps += 1

        # If we have reached the end, return the path and steps
        if (x, y) == end:
            return path + [(x, y)], steps

        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left

        for dx, dy in movements:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_path = path + [(x, y)]
                result, steps = dfs(new_x, new_y, new_path, steps)
                if result:
                    return result, steps

        return None, steps

    path, steps = dfs(start[0], start[1], [], 0)

    if path:
        return path, steps
    else:
        return "No path found to the exit.", steps


# Function to visualize the maze with 0, 1, and *


def visualize_maze(maze, path=None):
    for row in maze:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")  # Open path
            elif cell == 1:
                print("#", end=" ")  # Wall
            elif cell == 2:
                print(".", end=" ")  # Visited cell
            elif cell == 3:
                print("*", end=" ")  # Path
        print()

    if path:
        for x, y in path:
            maze[x][y] = 3  # Mark the path
        print("\n Shortest Path:")
        for row in maze:
            for cell in row:
                if cell == 0:
                    print(" ", end=" ")
                elif cell == 1:
                    print("#", end=" ")
                elif cell == 2:
                    print(".", end=" ")
                elif cell == 3:
                    print("*", end=" ")  # Path
            print()


# Example usage:
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0],
]

start = (0, 0)
end = (7, 8)

result, steps = solve_maze_dfs(maze, start, end)
if type(result) == list:
    visualize_maze(maze, result)
    print("\n Number of steps:", steps)
else:
    print(result)
