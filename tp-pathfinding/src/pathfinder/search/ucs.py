from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        explored[nodo.state] = nodo

        if nodo.state == grid.end: return Solution(nodo, explored)

        frontier: PriorityQueueFrontier = PriorityQueueFrontier()
        frontier.add(nodo, 0)
        while True:
            if frontier.is_empty(): break
            nodo = frontier.pop()
            if nodo.state == grid.end: return Solution(nodo, explored)
            neighbours = grid.get_neighbours(nodo.state)
            for position in neighbours:
                child = Node("", neighbours[position], nodo.cost + grid.get_cost(neighbours[position]), nodo, position)
                if child.state == grid.end: return Solution(child, explored)
                if child.state not in explored or child.cost < explored[child.state].cost:
                    explored[child.state] = child
                    frontier.add(child, child.cost)


        return NoSolution(explored)