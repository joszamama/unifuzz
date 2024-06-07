import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the desired mean and standard deviation for the normal distribution within the new range
DESIRED_MEAN = (120 + 20) / 2
DESIRED_STD = (120 - 20) / 6  # Assuming a range of 6 standard deviations for the normal distribution

# Define the evaluation function
def evalFitness(individual):
    mean_diff = abs(np.mean(individual) - DESIRED_MEAN)
    std_diff = abs(np.std(individual) - DESIRED_STD)
    return mean_diff + std_diff,

# Define the problem as a minimization (we want to minimize the difference from the desired mean and std dev)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Create the toolbox
toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_int", random.randint, 20, 120)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=50)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the evaluation, crossover, mutation, and selection functions
toolbox.register("evaluate", evalFitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=20, up=120, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm flow
def main():
    # Increase the population size
    pop = toolbox.population(n=100)
    
    # Increase the number of generations
    NGEN = 50000  # More iterations for better results
    CXPB, MUTPB = 0.5, 0.2
    
    # Define the statistics to be collected
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    
    # Run the Genetic Algorithm
    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, verbose=True)
    
    # Get the best individual
    best_ind = tools.selBest(pop, 1)[0]
    
    print(f"Best Individual: {best_ind}")
    print(f"Mean: {np.mean(best_ind)}, Std Dev: {np.std(best_ind)}")
    
    return best_ind

def plot_population(population):
    plt.figure(figsize=(10, 6))
    
    # Plot the histogram
    plt.hist(population, bins=15, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the normal distribution curve
    xmin, xmax = 20, 120
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, DESIRED_MEAN, DESIRED_STD)
    plt.plot(x, p, 'k', linewidth=2)
    
    plt.title('Histogram of the Best Population')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    best_population = main()
    plot_population(best_population)
