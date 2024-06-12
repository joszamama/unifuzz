import numpy as np
import statistics
import matplotlib.pyplot as plt

from collections import Counter
from fuzzingbook.GrammarFuzzer import GrammarFuzzer

from grammar.digit import DIGIT_GRAMMAR


def main():
    X = 10000

    results = []
    fuzzer = GrammarFuzzer(DIGIT_GRAMMAR)
    for i in range(X):
        input_str = fuzzer.fuzz()
        results.append(int(input_str))

    # Compute statistical data
    mean_value = statistics.mean(results)
    std_deviation = statistics.stdev(results)
    most_common_values = Counter(results).most_common(5)
    count_over_122 = sum(1 for x in results if x > 122)

    # Print the results
    print(f"Mean: {mean_value}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Most Common Values: {most_common_values}")
    print(f"Count of Instances Over 122: {count_over_122}")

    # Exclude values over 122

    results = [x for x in results if x <= 122]

    # Compute statistical data
    mean_value = statistics.mean(results)
    std_deviation = statistics.stdev(results)
    most_common_values = Counter(results).most_common(5)
    count_over_122 = sum(1 for x in results if x > 122)

    # Print the results
    print(f"Mean: {mean_value}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Most Common Values: {most_common_values}")
    print(f"Count of Instances Over 122: {count_over_122}")


if __name__ == "__main__":
    main()
