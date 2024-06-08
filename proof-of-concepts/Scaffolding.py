from fuzzingbook.GrammarFuzzer import EvenFasterGrammarFuzzer

from Grammar import JSON_GRAMMAR


def create_scaffolding(grammar: dict, inputs: int) -> list:
    input_set = []
    fuzzer = EvenFasterGrammarFuzzer(grammar)
    while len(input_set) < inputs:
        input_set.append(fuzzer.fuzz())
    return input_set


def instanciate_scaffolding(input_set: list, distributed_values: list, attribute: str) -> list:
    distributed_set = []
    for inp in input_set:
        string = inp.replace(attribute, str(distributed_values.pop(0)))
        distributed_set.append(string)
    return distributed_set


if __name__ == "__main__":
    input_set = create_scaffolding(JSON_GRAMMAR, 10)
    print(input_set)

    distributed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    distributed_set = instanciate_scaffolding(
        input_set, distributed_values, ">age<")
    print(distributed_set)
