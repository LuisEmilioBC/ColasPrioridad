import heapq

class ColaPrioridad:
    def __init__(self):
        self._cola = []
        self._indice = 0

    def push(self, dato, prioridad):
        heapq.heappush(self._cola, (-prioridad, self._indice, dato))
        self._indice += 1

    def pop(self):
        if self._cola:
            return heapq.heappop(self._cola)[-1]
        else:
            return "Ya no hay más tareas"