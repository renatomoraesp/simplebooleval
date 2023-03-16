# Evaluation Engine for Customizable Boolean Expressions

This Python project provides an evaluation engine for basic, yet customizable boolean expressions. The engine is designed to be versatile, allowing users to input a token dictionary and evaluate expressions with their own custom tokens, whitespace, and valid special tokens (i.e., logic operators). The engine is ideal for evaluating user-defined boolean expressions efficiently and accurately.

## Features

- Customizable token dictionary
- Supports whitespace and valid special tokens
- Includes common logic operators such as 'and', 'or', '<', '>', and other comparison operators
- Easy-to-use engine class for instantiating and evaluating expressions

## Getting Started

1. Clone the repository:
git` clone https://github.com/renatomoraesp/simplebooleval.git

2. Install the required packages:

pip install -r requirements.txt

3. Import the `EvaluationEngine` class:
```
from boolean_evaluation_engine import EvaluationEngine
```

4. Instantiate the engine with your custom token dictionary:
```
token_dict = {
    'A': True,
    'B': False,
    'C': True,
    # ...
}

engine = EvaluationEngine(token_dict)
```

5. Evaluate a boolean expression:

```
result = engine.evaluate_expression("A and B or not C")
print(result)  # Output: False
```

## Usage
Token Dictionary

The token dictionary must be provided by the user when instantiating the EvaluationEngine class. The dictionary maps each key to its corresponding boolean value, which will be used during the evaluation of the boolean expression.

Example:

```
token_dict = {
    'A': True,
    'B': False,
    'C': True,
    # ...
}
```

## Boolean Expressions

The engine evaluates boolean expressions containing keys from the token dictionary, whitespace, and valid special tokens. The special tokens include common logic operators such as 'and', 'or', 'not', '<', '>', and other comparison operators. To evaluate a boolean expression, simply pass the expression as a string to the evaluate_expression method:

```
result = engine.evaluate_expression("A and B or not C")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

