import distanceMatrix.DistanceMatrix as dm
from SimulatedAnneling import TSPProblem, simulated_annealing

def make_and_solve_tspproblem(cities, distances, n_iterations = 100):
  m = [cities, distances]

  problem = TSPProblem(m)
  best = simulated_annealing(problem, n_iterations)

  print("Melhor solução encontrada:", best)
  print("Valor da função:", problem.distance(best))

cities, distances = dm.read_distance_matrix("./distanceMatrix/distances")

print(f"Total cities: {cities}")

# E1:                Atroeira, Douro, Pinhal, Teixoso, Ulgueira, Vilar.
desired_cities_1 = ["Atroeira", "Douro", "Pinhal", "Teixoso", "Ulgueira", "Vilar"]
# E2:                Cerdeira, Douro, Gonta, Infantado, Lourel, Nelas, Oura, Quebrada, Roseiral, Serra, Teixoso, Ulgueira
desired_cities_2 = ["Cerdeira", "Douro", "Gonta", "Infantado", "Lourel", "Nelas", "Oura", "Quebrada", "Roseiral", "Serra", "Teixoso", "Ulgueira"]
# E3:                Belmar, Cerdeira, Douro, Encosta, Freita, Gonta, Horta, Infantado, Lourel, Monte, Nelas, Oura, Pinhal, Quebrada, Roseiral, Serra, Teixoso, Ulgueira.
desired_cities_3 = ["Belmar", "Cerdeira", "Douro", "Encosta", "Freita", "Gonta", "Horta", "Infantado", "Lourel", "Monte", "Nelas", "Oura", "Pinhal", "Quebrada", "Roseiral", "Serra", "Teixoso", "Ulgueira"]
# E4: todas as cidades
desired_cities_4 = cities

print(f"TSP cities: {desired_cities_1}")

n_iters = 10000;

print("Problem 1")
make_and_solve_tspproblem(desired_cities_1, distances, n_iters)
print("Problem 2")
make_and_solve_tspproblem(desired_cities_2, distances, n_iters)
print("Problem 3")
make_and_solve_tspproblem(desired_cities_3, distances, n_iters)
print("Problem 4")
make_and_solve_tspproblem(desired_cities_4, distances, n_iters)
