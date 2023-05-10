from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
        grid (Grid): Grid of points

        Returns:
        Solution: Solution found
        """
        # Initialize a node with the initial position
        nodo = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        explored[nodo.state] = True

        frontier = StackFrontier()

        frontier.add(nodo)

        while True:
            if frontier.is_empty(): break
            nodo = frontier.remove()
            if nodo.state == grid.end: return Solution(nodo, explored)
            neighbours = grid.get_neighbours(nodo.state)
            for position in neighbours:
                child = Node("", neighbours[position], nodo.cost + grid.get_cost(neighbours[position]), nodo, position)
                if child.state not in explored:
                    explored[child.state] = True
                    frontier.add(child)

        return NoSolution(explored)