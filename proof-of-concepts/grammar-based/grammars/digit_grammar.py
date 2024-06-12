from fuzzingbook.ProbabilisticGrammarFuzzer import opts


DIGIT_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": ["<digit>", "<digit><number>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

PROB_DIGIT_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": ["<digit>", ("<digit><number>", opts(prob=0.9))],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

MOD_DIGIT_GRAMMAR = {
    "<start>": ["<number>"],
    ("<number>", (1, 5000)): ["<digit>", "<digit><number>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
}
