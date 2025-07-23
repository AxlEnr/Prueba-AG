import pygad
import numpy

def fitness_func(solution, solution_idx):
    return numpy.sum(solution**2)

ga_instance = pygad.GA(num_generations=50,
                       sol_per_pop=10,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       gene_space=range(-10, 11),
                       num_genes=1,
                       mutation_probability=0.1)

ga_instance.run()
ga_instance.plot_fitness()
