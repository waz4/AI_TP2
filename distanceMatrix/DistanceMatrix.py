# Reads a distance matrix (composed of a list of cities and the matrix itself)
# given the file name f_name
def read_distance_matrix(f_name):
    cities = []
    distances = []

    with open(f_name, 'r') as f:
        i = 0
        for line in f:
            if i == 0:
                l = [line.rstrip().split()]
                city = l[0][1]
                cities.append(city)
            else:
                row = []
                l = [line.rstrip().split()]
                city = l[0][0]
                cities.append(city)
                j = 1
                while j <= i:
                    row.append(int(l[0][j]))
                    j += 1
                distances.append(row)
            i += 1

    return cities, distances


# Creates a distance matrix given another, m, and a list clist containing a
# subset of the cities occurring in m
def create_reduced_matrix(m, c_list):
    cities = c_list
    distances = []

    for c in range(1, len(cities)):
        row = []
        for v in range(0, c):
            row.append(distance(m, cities[c], cities[v]))
        distances.append(row)

    return cities, distances


# Creates a distance matrix given another, m, and a String, filter_, containing
# the initials of a subset of the cities occurring in m
def create_filter_matrix(m, filter_):
    return create_reduced_matrix(m, get_cities(m, filter_))


# Returns the distance between two cities c1 and c2, given distance matrix m
def distance(m, c1, c2):
    index1 = m[0].index(c1)
    index2 = m[0].index(c2)
    if index1 < index2:
        return m[1][index2 - 1][index1]
    else:
        return m[1][index1 - 1][index2]


# Presents the given distance matrix m
def show_distances(m):
    cities = '         '
    for i in range(0, len(m[0]) - 1):
        cities = cities + ' ' + "{:>9}".format(m[0][i])
    print(cities)
    for i in range(0, len(m[1])):
        row = "{:>9}".format(m[0][i + 1])
        for j in range(0, len(m[1][i])):
            row = row + ' ' + "{:>9}".format(m[1][i][j])
        print(row)


# Given a distance matrix m, returns a list of all the cites of m
def get_all_cities(m):
    return m[0]


# Given a distance matrix m and a String filter_, returns a subset of cites of m
# with initials in filter_
def get_cities(m, filter_):
    city_list = []
    for initial in filter_:
        city_list.append(get_city(m[0], initial))
    return city_list


# Given a list of cities cityList, returns the one with the first letter initial
def get_city(city_list, initial):
    for city in city_list:
        if city[0] == initial:
            return city


# Given a list of cities cityList, returns a String with their initials
def get_initials(city_list):
    initials = ""
    for city in city_list:
        initials += city[0]
    return initials
