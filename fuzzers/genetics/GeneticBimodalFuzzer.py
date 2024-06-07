import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the desired means and standard deviations for the bimodal distribution
MEAN1, STD1 = 25, 5
MEAN2, STD2 = 115, 5

# Define the evaluation function for the inverse normal distribution
def evalFitness(individual):
    # Calculate how well the individual's distribution matches the bimodal target distribution
    counts, bins = np.histogram(individual, bins=20, range=(20, 120), density=True)
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    # Calculate the expected densities from the two normal distributions
    pdf1 = norm.pdf(bin_centers, MEAN1, STD1)
    pdf2 = norm.pdf(bin_centers, MEAN2, STD2)
    target_pdf = (pdf1 + pdf2) / 2  # Combine the two distributions

    # Calculate the sum of squared differences between actual and target densities
    fitness = np.sum((counts - target_pdf) ** 2)
    return fitness,

# Define the problem as a minimization (we want to minimize the deviation from the inverse normal distribution)
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
    NGEN = 5000  # More iterations for better results
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
    plt.hist(population, bins=20, range=(20, 120), density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the target bimodal distribution curve
    x = np.linspace(20, 120, 100)
    pdf1 = norm.pdf(x, MEAN1, STD1)
    pdf2 = norm.pdf(x, MEAN2, STD2)
    target_pdf = (pdf1 + pdf2) / 2
    plt.plot(x, target_pdf, 'k', linewidth=2)
    
    plt.title('Histogram of the Best Population')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    best_population = main()
    plot_population(best_population)
