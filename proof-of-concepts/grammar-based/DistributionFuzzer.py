import random
import time

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer

from grammars.digit_grammar import DIGIT_GRAMMAR, PROB_DIGIT_GRAMMAR


def main():
    X = 10000

    results1 = []
    fuzzer = GrammarFuzzer(DIGIT_GRAMMAR)
    st_r1 = time.time()
    for i in range(X):
        input_str = fuzzer.fuzz()
        results1.append(len(input_str))
    t_r1 = time.time() - st_r1

    print("first fuzzer done")
    results2 = []
    st_r2 = time.time()
    fuzzer =  GrammarFuzzer(DIGIT_GRAMMAR, min_nonterminals=4)
    for i in range(X):
        input_str = fuzzer.fuzz()
        results2.append(len(input_str))
    t_r2 = time.time() - st_r2
    print("second fuzzer done")

    results3 = []
    st_r3 = time.time()
    fuzzer =  ProbabilisticGrammarFuzzer(PROB_DIGIT_GRAMMAR, min_nonterminals=4)
    for i in range(X):
        input_str = fuzzer.fuzz()
        results3.append(len(input_str))
    t_r3 = time.time() - st_r3
    print("third fuzzer done")

    # Count occurrences for each number of operators
    count1 = Counter(results1)
    count2 = Counter(results2)
    count3 = Counter(results3)

    # Combine all keys and sort them to make sure both fuzzers are compared at every possible count of operators
    all_keys = sorted(set(count1.keys()).union(set(count2.keys())).union(set(count3.keys())))

    # remove first value from all_keys
    all_keys = all_keys[1:]

    # Filter keys to include only values from 0 to 70
    all_keys = [k for k in all_keys if k >= 0 and k <= 52]

    frequencies1 = [count1[k] for k in all_keys]
    frequencies2 = [count2[k] for k in all_keys]
    frequencies3 = [count3[k] for k in all_keys]


    # Set bar width and positions
    bar_width = 0.35
    index = np.arange(len(all_keys))
    
    
    plt.figure(figsize=(12, 6))

    # Color Universal Design (CUD) Palette for color blindness
    cud_colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']

    plt.bar(index, frequencies1, bar_width, alpha=0.6, color=cud_colors[1], label=f'GrammarFuzzer in {t_r1:.2f}s')
    plt.bar(index + bar_width, frequencies2, bar_width, alpha=0.6, color=cud_colors[0], label=f'ExGrammarFuzzer in {t_r2:.2f}s')
    plt.bar(index + 2 * bar_width, frequencies3, bar_width, alpha=0.6, color=cud_colors[2], label=f'ExProbablisticFuzzer in {t_r3:.2f}s')

    plt.xlabel('Input Length', fontsize=10)
    plt.ylabel('Frequency', fontsize=10)
    plt.title('Distribution of Input Length (for ' + str(X) + ' inputs)', fontsize=10)
    
    plt.yticks(fontsize=10)

    # Or, show only every nth label on the x-axis
    n = 5  # Show every 5th label
    plt.xticks(index[::n] + bar_width / 2, all_keys[::n], rotation=-45, fontsize=13)
    plt.legend(fontsize=10)

    plt.tight_layout()
    plt.show()
    print("done")

if __name__ == "__main__":
    main()
