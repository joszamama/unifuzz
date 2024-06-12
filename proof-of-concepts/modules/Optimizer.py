import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt
from scipy.stats import norm


def generate_population(size, min_val, max_val, distribution, ngen, plot=False, verbose=False):
    # Define the desired distribution characteristics
    if distribution == 'normal':
        DESIRED_MEAN = (max_val + min_val) / 2
        # Assuming a range of 6 standard deviations
        DESIRED_STD = (max_val - min_val) / 6
    elif distribution == 'inverse_normal':
        MEAN1, STD1 = min_val + (max_val - min_val) * \
            0.1, (max_val - min_val) * 0.1
        MEAN2, STD2 = max_val - (max_val - min_val) * \
            0.1, (max_val - min_val) * 0.1

    # Define the evaluation function
    def evalFitness(individual):
        if distribution == 'normal':
            mean_diff = abs(np.mean(individual) - DESIRED_MEAN)
            std_diff = abs(np.std(individual) - DESIRED_STD)
            return mean_diff + std_diff,
        elif distribution == 'inverse_normal':
            counts, bins = np.histogram(
                individual, bins=20, range=(min_val, max_val), density=True)
            bin_centers = 0.5 * (bins[:-1] + bins[1:])
            pdf1 = norm.pdf(bin_centers, MEAN1, STD1)
            pdf2 = norm.pdf(bin_centers, MEAN2, STD2)
            target_pdf = (pdf1 + pdf2) / 2
            fitness = np.sum((counts - target_pdf) ** 2)
            return fitness,
        elif distribution == 'uniform':
            counts, _ = np.histogram(
                individual, bins=range(min_val, max_val + 1, 5))
            expected_count = len(individual) / len(counts)
            fitness = np.sum((counts - expected_count) ** 2)
            return fitness,

    # Define the problem as a minimization (we want to minimize the deviation from the desired distribution)
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    # Create the toolbox
    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("attr_int", random.randint, min_val, max_val)

    # Structure initializers
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.attr_int, n=size)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Register the evaluation, crossover, mutation, and selection functions
    toolbox.register("evaluate", evalFitness)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt,
                     low=min_val, up=max_val, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Genetic Algorithm flow
    def main():
        # Increase the population size
        pop = toolbox.population(n=100)

        # Number of generations
        NGEN = ngen
        CXPB, MUTPB = 0.5, 0.2

        # Define the statistics to be collected
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)

        # Run the Genetic Algorithm
        pop, logbook = algorithms.eaSimple(
            pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, verbose=verbose)

        # Get the best individual
        best_ind = tools.selBest(pop, 1)[0]

        print(f"Best Individual: {best_ind}")
        print(f"Mean: {np.mean(best_ind)}, Std Dev: {np.std(best_ind)}")

        return best_ind

    def plot_population(population):
        plt.figure(figsize=(10, 6))

        # Plot the histogram
        plt.hist(population, bins=20, range=(min_val, max_val),
                 density=True, alpha=0.6, color='g', edgecolor='black')

        # Plot the target distribution curve
        x = np.linspace(min_val, max_val, 100)
        if distribution == 'normal':
            p = norm.pdf(x, DESIRED_MEAN, DESIRED_STD)
            plt.plot(x, p, 'k', linewidth=2)
        elif distribution == 'inverse_normal':
            pdf1 = norm.pdf(x, MEAN1, STD1)
            pdf2 = norm.pdf(x, MEAN2, STD2)
            target_pdf = (pdf1 + pdf2) / 2
            plt.plot(x, target_pdf, 'k', linewidth=2)
        elif distribution == 'uniform':
            plt.axhline(y=1/(max_val-min_val), color='k',
                        linewidth=2)  # Uniform distribution line

        plt.title('Histogram of the Best Population')
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.grid(True)
        plt.show()

    best_population = main()

    if plot:
        plot_population(best_population)

    return best_population


if __name__ == "__main__":
    best_population = generate_population(30,
        min_val=20, max_val=80, distribution='normal', ngen=1000, plot=True)
    print(best_population)
