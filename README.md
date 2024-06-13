**Project Title: Shaping Test Inputs in Grammar-Based Fuzzing**

## Overview:

This repository contains the implementation of a grammar-based fuzzing tool designed to generate better-distributed tailored test suites. The tool leverages grammars and constraints extracted from programs to produce a specified number of valid inputs that meet the program's constraints and structure, effectively stressing the system based on chosen input feature distributions.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Experiments](#experiments)
- [Usage](#usage)
- [Related Work](#related-work)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Grammars serve as essential tools in computer science, particularly in areas such as natural language processing and programming language theory. In the context of software testing and security, grammars are used to define the structure of valid inputs for a system. This project aims to develop a tool that automatically generates better-distributed tailored test suites by leveraging grammars and constraints extracted from programs.

## Project Structure

The repository is organized as follows:

```
├── experiments
│   ├── 1-introduction
│   │   ├── grammar
│   │   │   ├── digit.py
│   │   └── AgeFuzzer.py
│   ├── 2-problem-description
│   │   ├── grammar
│   │   │   ├── digit.py
│   │   └── DistributionFuzzer.py
├── proof-of-concepts
│   ├── modules
│   │   ├── Optimizer.py
│   │   ├── Scaffolding.py
│   │   ├── Statistics.py
│   └── Fuzzer.py
├── resources
│   ├── constraints.txt
│   ├── grammar.py
├── related-work
│   ├── A quasi-polynomial-time algorithm for sampling words from a context-free language.pdf
│   ├── Automating grammar comparison.pdf
│   ├── Generating strings at random from a context free grammar.pdf
│   ├── Generating words in a context-free language uniformly at random.pdf
│   ├── Modular and efficient top-down parsing for ambiguous left recursive grammars.pdf
│   ├── On formal properties of simple phrase structure grammars.pdf
│   ├── The complexity of computing the number of strings of given length in context-free languages.pdf
│   ├── The Generation of Strings from a CFG using a Functional Language.pdf
│   ├── Uniform Random Generation of Strings in a Context-Free Language.pdf
│   ├── Uniform Random Sampling of Strings from Context-Free Grammar.pdf
├── .gitignore
├── README.md
├── requirements.txt
```

### Directories

- **experiments**: Contains scripts for initial experiments and problem descriptions.
- **proof-of-concepts**: Contains the core modules for the tool.
- **resources**: Includes grammar definitions and constraints files.
- **related-work**: Relevant research papers and documents.

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/joszamama/unifuzz.git
    cd unifuzz
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```


## Experiments

### Age Fuzzer Example

- The Age Fuzzer example in `experiments/1-introduction/AgeFuzzer.py` demonstrates how to generate values for an "Age" field in a web form. The example shows the bias introduced by traditional grammar-based fuzzing and highlights the benefits of our approach.

### Distribution Fuzzer Example

- The Distribution Fuzzer in `experiments/2-problem-description/DistributionFuzzer.py` illustrates the generation of inputs of the three state-of-the-art discussed methods, showcasing lack of diversity and the bias towards short inputs.

## Usage

### 1. Define the Grammar

Create a grammar file in the `resources` directory. Indicate the values to distribute with placeholders (e.g., `>value<`). For example:

```python
# grammar.py

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
```

### 2. Write the Constraints File

Create a `constraints.txt` file in the `resources` directory with the supported constraints, distribution, min value, and max value. Example format:

```
>age< distribution=uniform min=0 max=100
>budget< distribution=normal min=2000 max=8000
```

### 3. Run Proof-of-Concepts

The `proof-of-concepts` directory contains the core modules (`Optimizer.py`, `Scaffolding.py`, `Statistics.py`, `Fuzzer.py`). Follow these steps to use them:

1. **Create Scaffolding**:
   - Define the grammar and constraints.
   - Example grammar file: `resources/grammar.py`
   - Example constraints file: `resources/constraints.txt`

2. **Generate Population**:
   - Use the `Optimizer.py` module to generate a population based on the specified constraints.
   - Example usage:
     ```python
     from proof-of-concepts.modules.Optimizer import generate_population
     constraints = {
         '>age<': {'distribution': 'uniform', 'min_val': 0, 'max_val': 100},
         '>budget<': {'distribution': 'normal', 'min_val': 2000, 'max_val': 8000}
     }
     population = generate_population(30, constraints, ngen=1000, plot=True, verbose=True)
     print(population)
     ```

3. **Fuzzing**:
   - Use the `Fuzzer.py` module to integrate the scaffolding and generated population.
   - Example usage:
     ```python
     from proof-of-concepts.modules.Fuzzer import fuzz

     result = fuzz(
         grammar=JSON_GRAMMAR,
         inputs=100,
         constraints_file='resources/constraints.txt',
         plot=True,
         verbose=True
     )
     print(result)
     ```

4. **Additional Options**:
   - `plot`: Set to `True` to visualize the distribution of the generated population.
   - `verbose`: Set to `True` to enable detailed logging.
   - `ngen`: Number of generations for the genetic algorithm (default is 1000).

## Related Work

The `related-work` directory contains a collection of research papers that provide context and background for this project. These documents include foundational works on grammar-based fuzzing, context-free grammars, and related algorithms.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.