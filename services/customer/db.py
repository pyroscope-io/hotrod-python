from .client import Customer
import time
from services.maze.maze_manager import MazeManager
from services.maze.maze import Maze

def get_maze(width, height):
    manager = MazeManager()
    maze = manager.add_maze(width, height)

    # manager.solve_maze(maze.id, "BreadthFirst")
    # manager.solve_maze(maze.id, "BiDirectional")
    # manager.solve_maze(maze.id, "DepthFirstBacktracker")
    maze_image = manager.convert_maze_to_image(maze.id)

    return True

customers = {
    "123": Customer(id="123", name="Rachel's Floral Designs", location="115,277"),
    "567": Customer(id="567", name="Amazing Coffee Roasters", location="211,653"),
    "392": Customer(id="392", name="Trom Chocolatier", location="577,322"),
    "731": Customer(id="731", name="Japanese Deserts", location="728,326")
}

def get_customer_by_id(customer_id, mutex_delay=0):
    if customer_id not in customers: return

    if mutex_delay > 0:
        mutex_lock_delay(mutex_delay)

    print(f'mutex delay: #{mutex_delay}')

    return customers[customer_id]

def foo(weight):
    get_maze(weight, weight)

def bar(weight):
    get_maze(weight, weight)

def mutex_lock_delay(delay):
    if delay > 0:
        if delay == 1:
            foo(10)
        elif delay == 2:
            bar(10)

