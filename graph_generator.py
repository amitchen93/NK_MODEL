###########
# IMPORTS #
###########
import numpy as np
from collections import deque
from gene import Gene
from tqdm import tqdm
#############
# CONSTANTS #
#############
ALPHABET = {0: 0, 1: 1, 2: 2, 3: 3}
# ALPHABET = {0: 0, 1: 1, 2: 2}


def get_random_genotype(gene_length):
    return np.random.choice(list(ALPHABET.keys()), gene_length)


def calculate_gene_fitness(value):
    # return np.random.uniform(low=0, high=1, size=1)
    return 1



class GraphGenerator:
    def __init__(self, max_distance=3):
        self.max_distance = max_distance

    def get_neighbours(self, gene, value_to_gene):
        value = gene.get_value()
        neighbours = []
        for i in range(value.size):
            for letter in ALPHABET.keys():
                if value[i] == letter:
                    continue
                neighbour_value = value.copy()
                neighbour_value[i] = letter
                neighbour_key = tuple(neighbour_value)
                if neighbour_key in value_to_gene.keys():
                    neighbours.append(value_to_gene[neighbour_key])
                else:  # if the neighbour does not exist in current or previous rings it is gene of a further ring
                    if gene.get_distance() == self.max_distance:
                        continue
                    fitness = calculate_gene_fitness(value=neighbour_value)
                    neighbour = Gene(value=neighbour_value, fitness=fitness, distance=gene.get_distance() + 1)
                    neighbours.append(neighbour)
                    value_to_gene[neighbour_key] = neighbour
        return neighbours

    def generate_random_graph(self, gene_length):
        wild_type = get_random_genotype(gene_length)
        fitness = calculate_gene_fitness(wild_type)
        graph_root = Gene(value=wild_type, fitness=fitness, distance=0)
        value_to_gene = {tuple(wild_type): graph_root}
        q = deque()
        q.append(graph_root)
        dist_to_gene = {0: [graph_root]}
        fully_mapped_genes = set()
        while q:
            gene = q.popleft()
            if gene.get_distance() == self.max_distance:
                print()
            gene.neighbours = self.get_neighbours(gene=gene, value_to_gene=value_to_gene)
            for neighbour in tqdm(gene.get_neighbours()):
                if tuple(neighbour.value) in fully_mapped_genes:
                    continue
                q.append(neighbour)
            fully_mapped_genes.add(tuple(gene.value))

        print(value_to_gene)


if __name__ == '__main__':
    gg = GraphGenerator(max_distance=4)
    gg.generate_random_graph(7)
