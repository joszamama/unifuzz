JSON_GRAMMAR = {
    "<start>": ["{<json>}"],
    "<json>": ["<nameAttr>, <genderAttr>, <ageAttr>, <budgetAttr>"],
    "<nameAttr>": ['"Name": "<name>"'],
    "<genderAttr>": ['"Gender": "<gender>"'],
    "<ageAttr>": ['"Age": >age<'],
    "<budgetAttr>": ['"Budget": >budget<'],
    "<name>": ["John", "Jane", "Jim", "Jill", "Jack"],
    "<gender>": ["M", "F"],
}
