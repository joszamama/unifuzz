import time
import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

# Define the evaluation function for uniform distribution
def evalFitness(individual):
    counts, _ = np.histogram(individual, bins=range(20, 91, 5))  # Create bins for uniformity check
    expected_count = len(individual) / len(counts)  # Expected count per bin
    fitness = np.sum((counts - expected_count) ** 2)  # Sum of squared deviations from uniformity
    return fitness,

# Define the problem as a minimization (we want to minimize the deviation from uniform distribution)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Create the toolbox
toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_int", random.randint, 20, 90)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=50)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the evaluation, crossover, mutation, and selection functions
toolbox.register("evaluate", evalFitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=20, up=90, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm flow
def main():
    # Increase the population size
    pop = toolbox.population(n=100)
    
    # Increase the number of generations
    NGEN = 2500  # More iterations for better results
    CXPB, MUTPB = 0.5, 0.2
    
    # Define the statistics to be collected
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    # Start the timer
    st = time.time()
    # Run the Genetic Algorithm
    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, verbose=False)
    
    # Stop the timer
    t = time.time() - st
    print(f"Time taken: {t}")

    # Get the best individual
    best_ind = tools.selBest(pop, 1)[0]
    
    print(f"Best Individual: {best_ind}")
    print(f"Mean: {np.mean(best_ind)}, Std Dev: {np.std(best_ind)}")
    
    return best_ind

def plot_population(population):
    plt.figure(figsize=(10, 6))
    
    # Plot the histogram
    plt.hist(population, bins=range(10, 91, 5), density=True, alpha=0.6, color='g', edgecolor='black')
    
    plt.title('Histogram of the Best Population')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    best_population = main()
    plot_population(best_population)
