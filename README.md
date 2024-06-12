**Project Title: Shaping Test Inputs in Grammar-Based Fuzzing**

## Overview:

This repository contains the implementation of a grammar-based fuzzing tool designed to generate better-distributed tailored test suites. The tool leverages grammars and constraints extracted from programs to produce a specified number of valid inputs that meet the program's constraints and structure, effectively stressing the system based on chosen input feature distributions.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Experiments](#experiments)
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
│   │   └── AgeFuzzer.py
│   ├── 2-problem-description
│   │   └── DistributionFuzzer.py
├── grammars
│   ├── digit.py
│   └── json.py
├── proof-of-concepts
│   ├── modules
│   │   ├── Optimizer.py
│   │   ├── Scaffolding.py
│   │   └── Fuzzer.py
├── related-work
│   ├── A quasi-polynomial-time algorithm for sampling words from a context-free language.pdf
│   ├── Automating grammar comparison.pdf
│   ├── Generating strings at random from a context free grammar.pdf
│   ├── Generating words in a context-free language uniformly at random.pdf
│   ├── Modular and efficient top-down parsing for ambiguous left recursive grammars.pdf
│   ├── On formal properties of simple phrase structure grammars.pdf
│   ├── The complexity of computing the number of strings of given length in context-free languages.pdf
│   ├── The Generation of Strings from a CFG using a Functional Language.pdf
│   └── Uniform Random Generation of Strings in a Context-Free Language.pdf
│   └── Uniform Random Sampling of Strings from Context-Free Grammar.pdf
├── .gitignore
├── README.md
├── requirements.txt
```

### Directories

- **experiments**: Contains scripts for initial experiments and problem descriptions.
- **grammars**: Includes grammar definitions for different input types.
- **proof-of-concepts**: Contains the core modules for the tool.
- **related-work**: Relevant research papers and documents.

## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/grammar-based-fuzzing-tool.git
    cd grammar-based-fuzzing-tool
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

## Usage

1. **Run Experiments**:
    - Navigate to the `experiments` directory and run the scripts to see initial experiments and problem descriptions.
    - For example:
        ```sh
        python experiments/1-introduction/AgeFuzzer.py
        ```

2. **Use Core Modules**:
    - The `proof-of-concepts` directory contains the core modules (`Optimizer.py`, `Scaffolding.py`, `Fuzzer.py`). You can integrate these modules into your own scripts to generate tailored test suites.

## Experiments

### Age Fuzzer Example

- The Age Fuzzer example in `experiments/1-introduction/AgeFuzzer.py` demonstrates how to generate values for an "Age" field in a web form. The example shows the bias introduced by traditional grammar-based fuzzing and highlights the benefits of our approach.

### Distribution Fuzzer Example

- The Distribution Fuzzer in `experiments/2-problem-description/DistributionFuzzer.py` illustrates the generation of inputs with specific distributions, showcasing the tool's ability to produce more balanced and comprehensive test suites.

## Related Work

The `related-work` directory contains a collection of research papers that provide context and background for this project. These documents include foundational works on grammar-based fuzzing, context-free grammars, and related algorithms.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

By following these instructions, you should be able to set up, run, and extend the grammar-based fuzzing tool to fit your specific needs. For any questions or further assistance, please open an issue on GitHub.