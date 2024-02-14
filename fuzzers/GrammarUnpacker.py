

NUMBER_SIMPLE_GRAMMAR = {
    "<start>": ["<number>"],
    "<number>": [
        "<digit>", "<digit><number>"
    ],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}


def grammar_unpacker2(grammar: dict, depth: int) -> dict:
    """
    Unpack the grammar to a given depth. Using the grammar above and a depth of 3, the output should be:

    OUTPUT_GRAMMAR = {
        "<start>": ["<number>"],
        "<number>": [
            "<digit>", "<digit><digit>", "<digit><digit><digit>"
        ],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    }
    """
    pass

def grammar_unpacker(grammar: dict, depth: int) -> dict:
    """
    Unpack the grammar to a given depth.
    """
    unpacked_grammar = {}
    
    # Helper function to generate unpacked rules
    def unpack_rule(symbol, current_depth):
        if current_depth >= depth:
            return [symbol * depth]  # Return the symbol repeated to the depth
        unpacked_rule = []
        for item in grammar[symbol]:
            if item in grammar:
                unpacked_rule.extend(unpack_rule(item, current_depth + 1))
            else:
                unpacked_rule.append(item)
        return unpacked_rule

    for symbol in grammar:
        unpacked_grammar[symbol] = unpack_rule(symbol, 0)
    
    return unpacked_grammar


if __name__ == "__main__":
    TEST = grammar_unpacker(NUMBER_SIMPLE_GRAMMAR, 3)
    print(TEST)
