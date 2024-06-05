**Project Title: Towards a Distributed Input Space Exploration in Grammar-Based Fuzzing**

## Overview:

This project aims to enhance traditional grammar-based fuzzing techniques by introducing recursion depth control. By constraining the depth of recursion within the grammar, the approach prevents infinite expansion paths, leading to more efficient and effective fuzzing processes.

## Key Features:

- **Recursion Depth Control:** Limits recursion within the grammar to prevent infinite expansion paths.
- **Randomized Sampling:** Randomly selects expansion paths within defined recursion limits for variability in generated inputs.
- **Finite Exploration:** Transforms the input space from infinite to finite, facilitating thorough exploration during fuzzing.

## Installation:

To install the project, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/joszamama/unifuzz
   ```

2. Navigate to the project directory:

   ```
   cd unifuzz
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage:

1. Define the original grammar for the target function or program.
2. Modify the grammar to include recursion depth constraints.
3. Implement the fuzzing process using the modified grammar.
4. Run the fuzzing process to generate inputs within controlled recursion depths.

## How to add limits to the grammar:

```python
# Define the original grammar
original_grammar = {
    "<start>": ["{<json>}"],
    "<json>": ['"value": <number>'],
    "<number>": ["<digit><number>", "<digit>"],
    "<digit>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

# Modify the grammar with recursion depth constraints
modified_grammar = {
    "<start>": ["{<json>}"],
    "<json>": ['"value":<number>'],
    ("<number>", (1, 5000)): ["<digit>", "<digit><number>"],
    "<digit>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
}

```

## Contributions:

Contributions to the project are welcome! If you have any ideas for improvements or bug fixes, feel free to open an issue or submit a pull request.

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
