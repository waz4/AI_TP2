import math
import random
import DistanceMatrix as dm

cities, distances = dm.read_distance_matrix("distances")
m = [cities, distances]

class TSPProblem:
    def __init__(self, matrix):
        self.cidades, self.distances = dm.read_distance_matrix("distances")
        self.matrix = matrix
        self.cities = dm.get_all_cities(matrix)
        self.num_cities = len(self.cidades)

    def distance(self, route):
        total = 0
        for i in range(len(route) - 1):
            total += dm.distance(self.matrix, route[i], route[i+1])
        total += dm.distance(self.matrix, route[-1], route[0])  # volta à origem
        return total

problem = TSPProblem(m)

class Problem:
    def distance(self, sol):
        # Exemplo simples: função quadrática // alterar para a distanceMatrix
        return sol**2

def initial_sol(cities):
    return [random.randint(0, len(cities)) for _ in range(10)]

def neighbor(cities, j):
    # Remover se quisermos q o neighbor seja random, mas acho q devia ser outro metodo
    # i = random.randint(0, len(cities) - 3)
    # j = random.randint(i + 1, len(cities) - 1)
    i = 0
    if i == j:
        j = i + 2
    j = j % (len(cities) + 1)
    
    ret = cities.copy()
    
    temp = ret[i:j]
    temp_array = temp.copy()
    temp_array.reverse()
    
    for k in range(j):
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

def stopping_criteria(problema, melhor, T, n_iter):
    #Para a procura quando T tiver aquele dado valor
    return T < 1e-3

def simulated_annealing(
    problem,
    decay,
    initial_T,
    make_initial_sol,
    n_iter,
    var_n_iter,
    neighbor,
    stopping_criteria):

    # Inicializações
    current = make_initial_sol(problem)
    best = current
    T = initial_T(problem)


    # Loop principal // isto é o lagoritmo em si, não se deve alterar substancialmente
    while True:
        for _ in range(n_iter):
            proximo = neighbor(corrente)
            d = problem.distance(proximo) - problem.distance(corrente)

            if d < 0:
                corrente = proximo
                if problem.distance(corrente) < problem.distance(best):
                    best = corrente
            else:
                # Aceita solução pior com probabilidade exp(-d / T)
                if random.random() < math.exp(-d / T):
                    corrente = proximo
        # Critério de paragem
        if stopping_criteria(problem, best, T, n_iter):
            return best

        # Atualiza temperatura e número de iterações
        n_iter = var_n_iter(n_iter)
        T = decay(T)

problem = Problem()
best = simulated_annealing(
    problem,
    decay,
    initial_T,
    make_initial_sol=initial_sol,
    n_iter = 100,
    var_n_iter = var_n_iter,
    neighbor = neighbor,
    stopping_criteria = criterio_de_paragem)

print("Melhor solução encontrada:", best)
print("Valor da função:", problem.distancia(best))