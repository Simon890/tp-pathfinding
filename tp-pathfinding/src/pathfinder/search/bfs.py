from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
        grid (Grid): Grid of points

        Returns:
        Solution: Solution found
        """

        node = Node("", grid.start, 0)
        # # Initialize the explored dictionary to be empty
        explored = {}
        explored[node.state] = True

        if node.state == grid.end: return Solution(node, explored)

        frontier : QueueFrontier = QueueFrontier()

        frontier.add(node)
        while True:
            if frontier.is_empty(): return NoSolution(explored)
            nodo = frontier.remove()
            neighbours = grid.get_neighbours(nodo.state)
            explored[nodo.state] = True
            for position in neighbours:
                child = Node("", neighbours[position], nodo.cost + grid.get_cost(neighbours[position]), nodo, position)
                # print(explored)
                if child.state == grid.end: return Solution(child, explored)
                if child.state not in explored:
                    explored[child.state] = True
                    frontier.add(child)

        # Add the node to the explored dictionary

        return NoSolution(explored)