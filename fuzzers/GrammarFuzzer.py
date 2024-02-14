import matplotlib.pyplot as plt
from tqdm import tqdm
from fuzzingbook.ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer
from grammars.digit_simple import DIGIT_SIMPLE_GRAMMAR, NUMBER_SIMPLE_GRAMMAR, NUMBER_SIMPLE_PROBABILISTIC_GRAMMAR


def fuzz_grammar(grammar, iterations=1000):
    results = dict()
    length = dict()

    fuzzer = ProbabilisticGrammarFuzzer(grammar)
    for i in tqdm(range(iterations)):
        s = fuzzer.fuzz()
        for char in s:
            if char in results:
                results[char] += 1
            else:
                results[char] = 1
        if len(s) in length:
            length[len(s)] += 1
        else:
            length[len(s)] = 1



    plt.figure(figsize=(12, 6))

    # Subplot 1: Results plot
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, plot 1
    plt.xlabel("Digit chosen")
    plt.ylabel("Frequency (%)")
    plt.title(f'{iterations} inputs by GrammarFuzzer with NUMBER_SIMPLE_GRAMMAR')
    total_iterations = sum(results.values())
    percentages = [count / total_iterations *
                   100 for count in results.values()]
    # sort the result.keys in ascending order
    plt.bar(list(sorted(results.keys())), percentages)

    # Second Plot
    # Subplot 2: Length plot
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, plot 2
    plt.xlabel("Length")
    plt.ylabel("Frequency (%)")
    plt.title(f'{iterations} inputs by GrammarFuzzer with NUMBER_SIMPLE_GRAMMAR')
    # Assuming 'length' is a dictionary
    length = dict(sorted(length.items(), key=lambda item: item[0]))
    plt.bar(list(length.keys()), list(length.values()))

    plt.tight_layout()  # Automatically adjust subplot parameters to give specified padding
    plt.show()


def main():
    fuzz_grammar(NUMBER_SIMPLE_PROBABILISTIC_GRAMMAR, 1000000)


if __name__ == "__main__":
    main()
