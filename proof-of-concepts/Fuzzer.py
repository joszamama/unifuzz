from Grammar import JSON_GRAMMAR
from Scaffolding import create_scaffolding, instanciate_scaffolding
from Sampler import generate_population


def fuzz(grammar: dict, inputs: int, attribute: str, distribution: str, min_val: int, max_val: int, ngen: int, plot: bool = False, verbose: bool = False) -> list:
    scaffolding = create_scaffolding(grammar, inputs)
    distributed_values = generate_population(min_val, max_val, distribution, ngen, plot, verbose)
    return instanciate_scaffolding(scaffolding, distributed_values, attribute)

if __name__ == "__main__":
    distributed_list = fuzz(JSON_GRAMMAR, 10, ">age<", "normal", 20, 80, 1000, plot=True, verbose=True)
    print(distributed_list)