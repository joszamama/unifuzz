import random
import time
import matplotlib.pyplot as plt

from fuzzingbook.GrammarFuzzer import GrammarFuzzer

from grammars.digit_grammar import EXPR_GRAMMAR, MOD_EXPR_GRAMMAR


def extract_loops_and_exits(grammar: dict, key: tuple) -> dict:
    loop_nonterminals = []
    exit_nonterminals = []
    exit_terminals = []

    for keys in grammar.keys():
        if type(keys) is tuple:
            for pair in keys:
                if pair == key:
                    for nonterminal in grammar[keys]:
                        if "<" and ">" in nonterminal and key in nonterminal and "*" in nonterminal:
                            loop_nonterminals.append(nonterminal)
                        elif "<" and ">" in nonterminal and key not in nonterminal:
                            exit_nonterminals.append(nonterminal)
                        else:
                            exit_terminals.append(nonterminal)
        else:
            if keys == key:
                for nonterminal in grammar[keys]:
                    if "<" and ">" in nonterminal and key in nonterminal and "*" in nonterminal:
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

print(extract_loops_and_exits(MOD_EXPR_GRAMMAR, "<expr>"))

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
            elif len(repeatance) == 2 and preference == "low":
                expansions = random.randint(
                    repeatance[0], (repeatance[1] - repeatance[0]) / 3)
            elif len(repeatance) == 2 and preference == "center":
                expansions = random.randint(
                    repeatance[1] - repeatance[0] / 3, (repeatance[1] - repeatance[0]) / 1.5)
            elif len(repeatance) == 2 and preference == "high":
                expansions = random.randint(
                    (repeatance[1] - repeatance[0]) / 1.5, repeatance[1])

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
            elif len(repeatance) == 2 and preference == "low":
                expansions = random.randint(
                    1, (repeatance[1] - repeatance[0]) // 3)
            elif len(repeatance) == 2 and preference == "center":
                expansions = random.randint(
                    (repeatance[1] - repeatance[0]) // 2, (repeatance[1] - repeatance[0]) // 1.5)
            elif len(repeatance) == 2 and preference == "high":
                expansions = random.randint(repeatance[0], repeatance[1]*2)
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
    # Results for the first fuzzer
    results1 = []
    fuzzer = GrammarFuzzer(EXPR_GRAMMAR)
    st_r1 = time.time()
    for i in range(1000):
        results1.append(fuzzer.fuzz().count("*"))
    t_r1 = time.time() - st_r1

    print("first fuzzer done")
    # Results for the second fuzzer
    results2 = []
    X = 100000

    all_inputs = []
    low_inputs = []
    center_inputs = []
    high_inputs = []

    high_limit = 0
    low_limit = float('inf')  # Start with the largest possible number
    preference = "random"

    st_r2 = time.time()
    for i in range(X):
        print(preference)
        print(len(low_inputs), len(center_inputs), len(high_inputs))

        input_str = fuzz(MOD_EXPR_GRAMMAR, "high")
        results2.append(input_str.count("*"))

    
    print("second fuzzer done")

    t_r2 = time.time() - st_r2
    # Creating a subplot with 1 row and 2 columns
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plotting the first histogram
    axs[0].hist(results1, bins=10)
    axs[0].set_title('Histogram of SoA, in ' + str(t_r1) + "s")

    # Plotting the second histogram
    axs[1].hist(results2, bins=10)
    axs[1].set_title('Histogram of UniFuzz, in ' + str(t_r2) + "s")

    plt.show()
    print("done")


if __name__ == "__main__":
    main()