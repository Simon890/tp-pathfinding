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

        def h(nodo: tuple[int, int]):
            """
            Returns the cost in a straight line between
            the current node and the objective node,
            the euclidian distance

            Args: 
                Node.state: tuple(int, int)

            Returns: 
                float (distance)
            """
            x1, y1 = nodo[0], nodo[1]
            x2, y2 = grid.end[0], grid.end[1]

            return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)

        # inicializa la busqueda desde la raiz
        nodo = Node("", grid.start, 0)

        explored = {}
        explored[nodo.state] = nodo

        frontier = PriorityQueueFrontier()
        frontier.add(nodo, nodo.cost + h(nodo.state))

        while True:
            # recorre la frontera y elije un nodo
            if frontier.is_empty(): return NoSolution(explored)
            nodo = frontier.pop()

            if nodo.state == grid.end: return Solution(nodo, explored)
            neighbours = grid.get_neighbours(nodo.state)

            # exande el nodo seleccionado
            for position in neighbours:
                child = Node("", neighbours[position],
                             grid.get_cost(neighbours[position]),
                             nodo, position)
                
                # añade el nodo si no ha sido expandido antes, o si su costo es menor al mismo nodo ya expandido
                if child.state not in explored or child.cost < explored[child.state].cost:
                    explored[child.state] = child
                    frontier.add(child, child.cost + h(child.state))  # se guarda el nodo con su peso mas su respectivo valor heuristico
