import json
import time
from math import pi

from fuzzingbook.GrammarFuzzer import GrammarFuzzer, display_tree

from fuzzers.DistributionFuzzer import fuzz

valid_grammar = {
    "<start>": ["{<json>}"],
    "<json>": ['"value": <number>'],
    "<number>": ["<digit><number>", "<digit>"],
    "<digit>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

valid_mod_grammar = {
    "<start>": ["{<json>}"],
    "<json>": ['"value":<number>'],
    ("<number>", (1, 5000)): ["<digit>", "<digit><number>"],
    "<digit>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

def fuzz_soa(grammar: dict) -> str:
    fuzzer = GrammarFuzzer(grammar, min_nonterminals=5)
    return fuzzer.fuzz()

def fuzz_mine(grammar: dict) -> str:
    return fuzz(grammar, "random")

def process_json_file(valid_json):
    my_json = json.loads(valid_json)
    
    for key, value in my_json.items():
        if key == "value":
            result =  value ** 1

def test_soa(valid_grammar):
    valid_input = fuzz_soa(valid_grammar)
    process_json_file(valid_input)

def test_mine(valid_grammar):
    valid_input = fuzz_mine(valid_grammar)
    process_json_file(valid_input)

if __name__ == "__main__":
    inputs_mine = []
    start_time_mine = time.time()
    while True:
        try:
            test_mine(valid_mod_grammar)
            if len(inputs_mine) > 0:
                inputs_mine.append(time.time() - start_time_mine - inputs_mine[-1])
            else:
                inputs_mine.append(time.time() - start_time_mine)
        except Exception as e:
            print("Exception: " + str(e) + " in Mine")
            total_time_mine = time.time() - start_time_mine
            break

    print("Seconds taken for Mine: " + str(total_time_mine))
    print("#Inputs needed: " + str(len(inputs_mine)))
    print("Average time: " + str(sum(inputs_mine) / len(inputs_mine)))

    inputs_soa = []
    start_time_soa = time.time()
    while True:
        try:
            test_soa(valid_grammar)
            if len(inputs_soa) > 0:
                inputs_soa.append(time.time() - start_time_soa - inputs_soa[-1])
            else:
                inputs_soa.append(time.time() - start_time_soa)
        except Exception as e:
            print("Exception: " + str(e) + " in SOA")
            total_time_soa = time.time() - start_time_soa
            break
    
    print("Seconds taken for SOA: " + str(total_time_soa))
    print("#Inputs needed: " + str(inputs_soa))
    print("Average time: " + str(sum(inputs_soa) / len(inputs_soa)))