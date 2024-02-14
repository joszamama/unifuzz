from fuzzingbook.ProbabilisticGrammarFuzzer import opts

DIGIT_SIMPLE_GRAMMAR = {
    "<start>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

NUMBER_SIMPLE_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": [
        "<digit>", "<digit><number>"
    ],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

NUMBER_SIMPLE_PROBABILISTIC_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": [
        ("<digit>", opts(prob=0.1)), ("<digit><number>", opts(prob=0.9))
    ],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

NUMBER_UNPACKED_GRAMMAR_D3 = {
    "<start>": ["<number>"],
    "<number>": [
        "<digit>", "<digit><digit>", "<digit><digit><digit>"
    ],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

{'<start>': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<digit><number>'], '<number>': ['0', '1', '2', '3',
                                                                                                '4', '5', '6', '7', '8', '9', '<digit><number>'], '<digit>': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}
