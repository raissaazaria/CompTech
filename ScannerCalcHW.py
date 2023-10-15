import re


def tokenize_calculator_input(input_string):
    # Define regular expressions for different token types
    token_patterns = [
        (r'([a-zA-Z_][a-zA-Z0-9_]*)', 'id'),  # Identifier (e.g., Celcius, Fahrenheit)
        (r':=', 'assign'),  # Assignment operator :=
        (r'([0-9]+\.[0-9]+|[0-9]+)', 'number'),  # Number (integer or float)
        (r'\(', 'lparen'),  # Left parenthesis (
        (r'\)', 'rparen'),  # Right parenthesis )
        (r'\*', 'times'),  # Multiplication operator *
        (r'/', 'div'),  # Division operator /
        (r'\+', 'plus'),  # Addition operator +
        (r'\s+', None),  # Whitespace (to be ignored)
    ]

    tokens = [] # Initialize an empty list to store the tokens

    while input_string:  # Iterate through the input string and tokenize it
        matched = False
        for pattern, token_type in token_patterns:
            regex = re.compile('^' + pattern)
            match = regex.search(input_string)
            if match:
                value = match.group(0)
                if token_type is not None:  # Ignore whitespace tokens
                    tokens.append((token_type, value))
                input_string = input_string[len(value):]
                matched = True
                break

        if not matched:
            raise ValueError(f"Invalid input: {input_string}")

    return tokens


input_expression = input("Enter a custom calculator expression: ")

tokens = tokenize_calculator_input(input_expression) # Tokenize the input expression

for token_type, value in tokens:
    print(f"{token_type}: {value}")
