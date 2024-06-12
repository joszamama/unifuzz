from fuzzingbook.ProbabilisticGrammarFuzzer import opts

EXPR_GRAMMAR = {
    "<start>": ["<expr>"],
    "<expr>": ["<term> + <expr>", "<term> - <expr>", "<expr> * <term>", "<expr> / <term>", "<term>", "(<expr>)"],
    "<term>": ["<integer>.<integer>", "<integer>"],
    "<integer>": ["<digit><integer>", "<digit>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

MOD_EXPR_GRAMMAR = {
    "<start>": ["<expr>"],
    ("<expr>", (1, 75)): ["<term>+<expr>", "<term>"],
    "<term>": ["<integer>"],
    "<integer>": ["<digit>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

MOD_EXPR_GRAMMAR_1 = {
    "<start>": ["<expr>"],
    ("<expr>", (7, 23)): ["<term> + <expr>", "<term> - <expr>", "<term> * <expr>", "<term> / <expr>", "<term>", "(<expr>)", "<expr> / <term> * <expr>"],
    "<term>": ["+<term>", "-<term>", "<integer>.<integer>", "<integer>"],
    "<integer>": ["<digit><integer>", "<digit>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

MOD_EXPR_GRAMMAR_2 = {
    "<start>": ["<expr>"],
    ("<expr>", (3, 10, 15, 23)): ["<term> + <expr>", "<term> - <expr>", "<term> * <expr>", "<term> / <expr>", "<term>", "(<expr>)", "<expr> / <term> * <expr>"],
    "<term>": ["+<term>", "-<term>", "<integer>.<integer>", "<integer>"],
    "<integer>": ["<digit><integer>", "<digit>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}