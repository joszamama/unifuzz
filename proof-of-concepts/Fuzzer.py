from grammars.json import JSON_GRAMMAR
from modules.Scaffolding import create_scaffolding, instanciate_scaffolding
from modules.Optimizer import generate_population


def fuzz(grammar: dict, inputs: int, attribute: str, distribution: str, min_val: int, max_val: int, ngen: int, plot: bool = False, verbose: bool = False) -> list:
    scaffolding = create_scaffolding(grammar, inputs)
    distributed_values = generate_population(inputs, min_val, max_val, distribution, ngen, plot, verbose)
    return instanciate_scaffolding(scaffolding, distributed_values, attribute)

if __name__ == "__main__":
    distributed_list = fuzz(JSON_GRAMMAR, 100, ">age<", "uniform", 20, 120, 1, plot=False, verbose=False)
    print(distributed_list)
