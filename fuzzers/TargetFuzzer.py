from Levenshtein import distance

from fuzzingbook.GrammarFuzzer import GrammarFuzzer

from fuzzers.grammars.digit_grammar import NUMBER_SIMPLE_GRAMMAR
from grammars.sql_grammar import SQL_GRAMMAR


def grammar_fuzzer(grammar: dict, generate=1000):
    fuzzer = GrammarFuzzer(grammar)
    inputs = []
    for _ in range(generate):
        inp = fuzzer.fuzz()
        inputs.append(inp)
    return inputs


def target_fuzzer(grammar: dict, generate=1000, threshold=10):
    fuzzer = GrammarFuzzer(grammar)
    inputs = []
    discard = []
    while len(inputs) < generate:
        inp = fuzzer.fuzz()
        if len(inputs) == 0:
            inputs.append(inp)
        else:
            for i in inputs:
                if distance(i, inp) < threshold:
                    discard.append(inp)
                    break
            else:
                inputs.append(inp)
    return inputs, discard


def main():
    inputs = grammar_fuzzer(SQL_GRAMMAR, generate=100)
    for inp in inputs:
        print(inp)

    print("\n\n\n")

    inputs, _ = target_fuzzer(SQL_GRAMMAR, generate=100, threshold=70)
    for inp in inputs:
        print(inp)


if __name__ == "__main__":
    main()
