# Neighor random? y é random

import math
import random
import distanceMatrix.DistanceMatrix as dm

class TSPProblem:
    def __init__(self, matrix):

        self.matrix = matrix
        self.cities = dm.get_all_cities(matrix)
        self.num_cities = len(self.cities)

    # Route é um array de cidades
    def distance(self, route):
        total = 0
        for i in range(len(route) - 1):
            total += dm.distance(self.matrix, route[i], route[i+1])
        total += dm.distance(self.matrix, route[-1], route[0])  # volta à origem
        return total

# Mudar para fazer com subsets das cidades
def initial_sol(cities):
    route = cities.copy()
    random.shuffle(route)
    return route

# Verificar se e circlar
# TODO FIX THIS SHIT
def neighbor(cities):
    # Remover se quisermos q o neighbor seja random, mas acho q devia ser outro metodo
    i = random.randint(0, len(cities) - 3)
    j = random.randint(i + 1, len(cities) - 1)
    
    if i == j:
        j = i + 2
    
    j = j % (len(cities) + 1)
    
    ret = cities.copy()
    
    temp = ret[i:j]
    temp_array = temp.copy()
    temp_array.reverse()
    
    for k in range(len(temp_array)):
      ret[i + k] = temp_array[k]
    
    return ret

def initial_T(problem):
    #pode-se alterar para algum outro valor/função que decida que valor a temperatura deve ter
    return 100.0

def decay(T):
    #isto vai ficar igual probably
    return T * 0.95

def var_n_iter(n):
    return n

def stopping_criteria(problem, melhor, T, n_iter):
    #Para a procura quando T tiver aquele dado valor
    return T < 1e-3

def simulated_annealing(
    problem: TSPProblem,
    n_iter: int = 100,
    decay = decay,
    initial_T = initial_T,
    make_initial_sol = initial_sol,
    var_n_iter = var_n_iter,
    neighbor = neighbor,
    stopping_criteria = stopping_criteria
    ):

    # Inicializações
    current = make_initial_sol(problem.cities)
    best = current
    T = initial_T(problem)

    # Loop principal isto é o lagoritmo em si, não se deve alterar substancialmente
    while True:
        for j in range(n_iter):
            next = neighbor(current)
            d = problem.distance(next) - problem.distance(current)

            if d < 0:
                current = next
                if problem.distance(current) < problem.distance(best):
                    best = current
            else:
                # Aceita solução pior com probabilidade exp(-d / T)
                if random.random() < math.exp(-d / T):
                    current = next
        # Critério de paragem
        if stopping_criteria(problem, best, T, n_iter):
            return best

        # Atualiza temperatura e número de iterações
        n_iter = var_n_iter(n_iter)
        T = decay(T)
