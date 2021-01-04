from maze.maze_manager import MazeManager
from maze.maze import Maze

def get_maze():
    manager = MazeManager()
    maze = manager.add_maze(15, 15)

    # manager.solve_maze(maze.id, "BreadthFirst")
    # manager.solve_maze(maze.id, "BiDirectional")
    # manager.solve_maze(maze.id, "DepthFirstBacktracker")
    maze_image = manager.convert_maze_to_image(maze.id)

    return True

if __name__ == "__main__":
    get_maze()
