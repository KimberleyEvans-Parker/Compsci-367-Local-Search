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
    results["time"] = finish - start
    return results


def average_std(problem, function, number):
    print("-" * 10 + str(function).upper().split(" ")[1] + "-" * 10)
    times = []
    num_exanded_nodes = []
    solved = 0
    for i in range(number):
        results = time_function(problem, function)
        times.append(results["time"])
        num_exanded_nodes.append(results["expanded"])
        if results["solved"]:
            solved += 1
    time_standard_deviation = numpy.std(times)
    time_average = numpy.average(times)
    expanded_standard_deviation = numpy.std(num_exanded_nodes)
    expanded_average = numpy.average(num_exanded_nodes)
    solving_probability = solved / number
    print("expanded: {0:.5f} +- {1:.5f}".format(expanded_average,
                                                expanded_standard_deviation))
    print("time: {0:.5f} +- {1:.5f}".format(time_average,
                                            time_standard_deviation))
    print("solving_probability: ", solving_probability)


NUM_TRIALS = 1000
NUM_QUEENS = 15

for i in range(NUM_QUEENS, NUM_QUEENS + 3):
    print("N:", i)
    problem = NQueensProblem(N=i)
    average_std(problem, hill_climbing_instrumented, NUM_TRIALS)
    average_std(problem, hill_climbing_sideways, NUM_TRIALS)
    average_std(problem, hill_climbing_random_restart, NUM_TRIALS)
    print()
