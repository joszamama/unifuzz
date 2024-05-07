import random
import time
import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

from fuzzingbook.GrammarFuzzer import GrammarFuzzer

from grammars.digit_grammar import MOD_DIGIT_GRAMMAR, DIGIT_GRAMMAR, EXPR_GRAMMAR, MOD_EXPR_GRAMMAR, MOD_EXPR_GRAMMAR_1, MOD_EXPR_GRAMMAR_2


def extract_loops_and_exits(grammar: dict, key: tuple) -> dict:
    loop_nonterminals = []
    exit_nonterminals = []
    exit_terminals = []

    for keys in grammar.keys():
        if type(keys) is tuple:
            for pair in keys:
                if pair == key:
                    for nonterminal in grammar[keys]:
                        if "<" and ">" in nonterminal and key in nonterminal:
                            loop_nonterminals.append(nonterminal)
                        elif "<" and ">" in nonterminal and key not in nonterminal:
                            exit_nonterminals.append(nonterminal)
                        else:
                            exit_terminals.append(nonterminal)
        else:
            if keys == key:
                for nonterminal in grammar[keys]:
                    if "<" and ">" in nonterminal and key in nonterminal:
                        loop_nonterminals.append(nonterminal)
                    elif "<" and ">" in nonterminal and key not in nonterminal:
                        exit_nonterminals.append(nonterminal)
                    else:
                        exit_terminals.append(nonterminal)

    return {
        "all_options": loop_nonterminals + exit_nonterminals + exit_terminals,
        "all_exits": exit_nonterminals + exit_terminals,
        "loop_nonterminals": loop_nonterminals,
        "exit_nonterminals": exit_nonterminals,
        "exit_terminals": exit_terminals
    }


def get_repeteance_tuple(grammar: dict, key: tuple) -> tuple:
    for keys in grammar.keys():
        for pair in keys:
            if pair == key:
                return keys[1]
    return ()


def complete_word(grammar: dict, word: str, depth: int) -> str:
    levels = {}
    level = 1
    for key in grammar.keys():
        levels[level] = key
        level += 1

    try:
        token_to_replace = levels[depth][0]
        while token_to_replace in word:
            replacement = random.choice(extract_loops_and_exits(
                grammar, (token_to_replace))["all_exits"])
            word = word.replace(token_to_replace, replacement, 1)
    except:
        token_to_replace = levels[depth]
        while token_to_replace in word:
            replacement = random.choice(extract_loops_and_exits(
                grammar, (token_to_replace))["all_exits"])
            word = word.replace(token_to_replace, replacement, 1)
    return word


def get_tree_level(grammar: dict, depth: int) -> tuple:
    levels = {}
    level = 1
    for key in grammar.keys():
        levels[level] = key
        level += 1

    return levels[depth]


def fuzz(grammar: dict, preference: str) -> str:
    is_first_string_completed = False
    is_word_completed = False
    level = 1
    word = ""
    start_token = "<start>"
    while not is_first_string_completed:
        repeatance = get_repeteance_tuple(grammar, (start_token))
        if repeatance == () or repeatance == None:
            word += random.choice(extract_loops_and_exits(grammar,
                                                          (start_token))["all_options"])
        else:
            if len(repeatance) == 4 and preference == "random":
                low_l1 = repeatance[0]
                low_l2 = repeatance[1]
                up_l1 = repeatance[2]
                up_l2 = repeatance[3]

                # generate a random number between low_l1 and low_l2
                random_number1 = random.randint(low_l1, low_l2 - 1)
                # generate a random number between up_l1 and up_l2
                random_number2 = random.randint(up_l1, up_l2)

                # pick randomly either random_number1 or random_number2
                choice = random.choice([random_number1, random_number2])
                expansions = choice
            elif len(repeatance) == 2 and preference == "random":
                expansions = random.randint(repeatance[0], repeatance[1])

            while expansions > 1:
                word += random.choice(extract_loops_and_exits(grammar,
                                                              (start_token))["loop_nonterminals"])
                expansions -= 1
            word += random.choice(extract_loops_and_exits(grammar,
                                                          (start_token))["all_exits"])
        is_first_string_completed = True
        level += 1
        next_token = get_tree_level(grammar, level)
        if next_token[0] == "<":
            start_token = next_token
        else:
            start_token = next_token[0]

    while not is_word_completed:
        repeatance = get_repeteance_tuple(grammar, (start_token))
        if repeatance == () or repeatance == tuple():
            while start_token in word:
                word = word.replace(start_token, random.choice(
                    extract_loops_and_exits(grammar, (start_token))["all_options"]), 1)
            word = complete_word(grammar, word, level)
        else:
            if len(repeatance) == 4:
                low_l1 = repeatance[0]
                low_l2 = repeatance[1]
                up_l1 = repeatance[2]
                up_l2 = repeatance[3]
                # generate a random number between low_l1 and low_l2
                random_number1 = random.randint(low_l1, low_l2 - 1)
                # generate a random number between up_l1 and up_l2
                random_number2 = random.randint(up_l1, up_l2)

                # pick randomly either random_number1 or random_number2
                choice = random.choice([random_number1, random_number2])
                expansions = choice
            elif len(repeatance) == 2 and preference == "random":
                expansions = random.randint(repeatance[0], repeatance[1])

            while expansions > 1:
                word = word.replace(start_token, random.choice(
                    extract_loops_and_exits(grammar, (start_token))["loop_nonterminals"]), 1)
                expansions -= 1
            word = word.replace(start_token, random.choice(
                extract_loops_and_exits(grammar, (start_token))["all_exits"]), 1)
            word = complete_word(grammar, word, level)

        if "<" not in word:
            is_word_completed = True
        else:
            level += 1
            next_token = get_tree_level(grammar, level)
            if next_token[0] == "<":
                start_token = next_token
            else:
                start_token = next_token[0]

    return word

def main():
    X = 20000

    results1 = []
    fuzzer = GrammarFuzzer(EXPR_GRAMMAR)
    st_r1 = time.time()
    for i in range(X):
        input_str = fuzzer.fuzz()
        results1.append(len(input_str))
    t_r1 = time.time() - st_r1

    print("first fuzzer done")
    results2 = []
    st_r2 = time.time()
    for i in range(X):
        input_str = fuzz(MOD_EXPR_GRAMMAR, "random")
        results2.append(len(input_str))
    t_r2 = time.time() - st_r2

    # Count occurrences for each number of operators
    count1 = Counter(results1)
    count2 = Counter(results2)

    # Combine all keys and sort them to make sure both fuzzers are compared at every possible count of operators
    all_keys = sorted(set(count1.keys()).union(set(count2.keys())))
    frequencies1 = [count1[k] for k in all_keys]
    frequencies2 = [count2[k] for k in all_keys]

    # Set bar width and positions
    bar_width = 0.35
    index = np.arange(len(all_keys))

    plt.figure(figsize=(12, 6))
    plt.bar(index, frequencies1, bar_width, alpha=0.6, color='skyblue', label=f'SoA in {t_r1:.2f}s')
    plt.bar(index + bar_width, frequencies2, bar_width, alpha=0.6, color='salmon', label=f'UniFuzz in {t_r2:.2f}s')

    plt.xlabel('# of Multiplications', fontsize=25)
    plt.ylabel('Frequency')
    plt.title('Distribution of # of Multiplications')
    plt.yticks(fontsize=15)
    plt.xticks(index + bar_width / 2, all_keys, rotation=-45, fontsize=15)  # Positioning the ticks
    plt.legend(fontsize=25)
    plt.tight_layout()
    plt.show()
    print("done")

# Remember to check the imports and module specifics based on your actual working environment.



if __name__ == "__main__":
    main()
