from hill_climbing import (
    NQueensProblem,
    hill_climbing_instrumented,
    hill_climbing_sideways,
    hill_climbing_random_restart,
)

# import timeit
import numpy
import time


def time_function(problem, function):
    problem2 = NQueensProblem(state=problem.random_state())
    start = time.time()
    results = function(problem2)
    finish = time.time()
    results["time_to_solve"] = finish - start
    return results


problem = NQueensProblem(N=10)
problem2 = NQueensProblem(state=problem.random_state())
results = hill_climbing_instrumented(problem2)

print("expanded: ", results["expanded"])
print("solved: ", results["solved"])
# print("expanded: ", results["expanded"])

# print(numpy.std([10, 12, 23, 23, 16, 23, 21, 16]))
# print(numpy.average([10, 2, 38, 23, 38, 23, 21]))

print(time_function(problem, hill_climbing_instrumented))
