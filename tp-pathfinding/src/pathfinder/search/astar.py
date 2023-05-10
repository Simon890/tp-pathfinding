from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
        grid (Grid): Grid of points

        Returns:
        Solution: Solution found
        """

        def h(nodo1 : tuple[int, int]):
            """
            Función Heurística
            Retorna el costo del nodo 1
            """
            x1 = nodo1[0]
            y1 = nodo1[1]
            x2 = grid.end[0]
            y2 = grid.end[1]
            return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

        # Initialize a node with the initial position
        nodo = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        explored[nodo.state] = nodo

        frontier = PriorityQueueFrontier()

        frontier.add(nodo, 0)
        while True:
            if frontier.is_empty(): break
            nodo = frontier.pop()
            if nodo.state == grid.end: return Solution(nodo, explored)
            neighbours = grid.get_neighbours(nodo.state)
            for position in neighbours:
                child = Node("", neighbours[position], grid.get_cost(neighbours[position]) + h(neighbours[position]), nodo, position)
                if child.state not in explored or child.cost < explored[child.state].cost:
                    explored[child.state] = child
                    frontier.add(child, child.cost)

        return NoSolution(explored)