import numpy as np
from numpy.linalg import svd


def balance_equation(composition_matrix):
    u, d, _ = svd(composition_matrix)

    solution = u[:, -1]
    solution /= min(np.abs(solution))
    return solution


if __name__ == "__main__":
    # FeCl3 + MgO ---> Fe2O3 + MgCl2
    a = np.array([[1, 3, 0, 0], [0, 0, 1, 1], [2, 0, 0, 3], [0, 2, 1, 0]])
    # 2FeCl3 + 3MgO ---> Fe2O3 + 3MgCl2
    print(balance_equation(a))

    # C5H11NH2 + O2 ---> CO2 + H2O + NO2
    a = np.array([[5, 13, 1, 0], [0, 0, 0, 2], [1, 0, 0, 2], [0, 2, 0, 1], [0, 0, 1, 2]])
    # 4C5H11NH2 + 37O2 ---> 20CO2 + 26H2O + 4NO2
    print(balance_equation(a))