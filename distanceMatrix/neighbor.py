import random, DistanceMatrix

# Algoritmo de vizinhança do guiao2: https://ia.ssdi.di.fct.unl.pt/guiao2.html
def neighbor(cities):
    # Remover se quisermos q o neighbor seja random, mas acho q devia ser outro metodo
    # i = random.randint(0, len(cities) - 3)
    # j = random.randint(i + 1, len(cities) - 1)
    # i = 0
    # 
    # if i == j:
    #    j = i + 2
    #
    #j = j % (len(cities) + 1)
    #
    #ret = cities.copy()
    #
    #temp = ret[i:j]
    #temp_array = temp.copy()
    #temp_array.reverse()
    #
    #for k in range(len(temp_array)):
    #  ret[i + k] = temp_array[k]
    #
    #return ret
    n = len(cities)
    if n < 2:
        return cities.copy()  # Não há vizinhos possíveis
    i = random.randint(0, n - 2)
    j = random.randint(i + 1, n - 1)

    ret = cities.copy()
    ret[i:j+1] = reversed(ret[i:j+1])
    return ret  # Troca as cidades nas posições i e j


# Exemplo de como usar

matrix = DistanceMatrix.read_distance_matrix("distances")
cities = DistanceMatrix.get_all_cities(matrix)

# print(cities)

for i in range(0, len(cities) + 4):
  print(neighbor(cities))

print()