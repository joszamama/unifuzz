from modules.Scaffolding import create_scaffolding, instanciate_scaffolding
from modules.Optimizer import read_constraints, generate_population
from modules.Statistics import compute_metrics

from resources.grammar import JSON_GRAMMAR

def fuzz(grammar: dict, inputs: int, constraints_file: str, ngen: int = 1000, plot: bool = False, verbose: bool = False, statistics: bool = False) -> list:
    constraints = read_constraints(constraints_file)
    scaffolding = create_scaffolding(grammar, inputs)
    populations = generate_population(inputs, constraints, ngen=ngen, plot=plot, verbose=verbose)
    
    for attribute, values in populations.items():
        scaffolding = instanciate_scaffolding(scaffolding, values, attribute)

    if statistics:
        metrics = compute_metrics(scaffolding)
        print(metrics)

    return scaffolding


if __name__ == "__main__":
    result = fuzz(JSON_GRAMMAR, 1000, './proof-of-concepts/resources/constraints.txt', 10000, plot=True, verbose=True, statistics=True)
    print(result)
