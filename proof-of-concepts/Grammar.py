from fuzzingbook.GrammarFuzzer import EvenFasterGrammarFuzzer

JSON_GRAMMAR = {
    "<start>": ["{<json>}"],
    "<json>": ["<nameAttr>, <genderAttr>, <ageAttr>"],
    "<nameAttr>": ['"Name": "<name>"'],
    "<genderAttr>": ['"Gender": "<gender>"'],
    "<ageAttr>": ['"Age": >age<'],
    "<name>": ["John", "Jane", "Jim", "Jill", "Jack"],
    "<gender>": ["M", "F"],
}

if __name__ == "__main__":
    fuzzer = EvenFasterGrammarFuzzer(JSON_GRAMMAR)
    print(fuzzer.fuzz())
