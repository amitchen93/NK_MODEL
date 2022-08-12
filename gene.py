class Gene:

    def __init__(self, value, fitness=None, distance=None, neighbours=None):
        self.value = value
        self.fitness = fitness
        self.distance = distance
        self.neighbours = neighbours

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_value(self):
        return self.value

    def get_distance(self):
        return self.distance

    def get_neighbours(self):
        return self.neighbours

    def __repr__(self):
        if self.distance == 0:
            return f'Wild Type Gene {self.value}, fitness:{self.fitness}'
        return f'gene: {self.value}, fitness: {self.fitness}, distance: {self.distance}'

    def __str__(self):
        if self.distance == 0:
            return f'Wild Type Gene {self.value}, fitness:{self.fitness}'
        return f'gene: {self.value}, fitness: {self.fitness}, distance: {self.distance}'
