def tokenize_calculator_input(input_string):
    tokens = []
    current_token = ""

    for char in input_string:
        if char.isalpha():
            # Handle identifiers (e.g., Celcius, Fahrenheit)
            current_token += char
        elif char.isdigit() or char == '.':
            # Handle numbers (e.g., 100.0)
            current_token += char
        elif char in ['=', '+', '-', '*', '/', '(', ')']:
            # Handle operators and parentheses
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)

    # Add the last token if present
    if current_token:
        tokens.append(current_token)

    return tokens


while True:
    user_input = input("Enter an expression (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    tokens = tokenize_calculator_input(user_input)

    token_types = {
        ':=': 'assign',
        '+': 'plus',
        '-': 'minus',
        '*': 'times',
        '/': 'div',
        '(': 'lparen',
        ')': 'rparen'
    }

    print("Tokens:")
    for token in tokens:
        if token in token_types:
            print(f"{token_types[token]}: {token}")
        elif token.isnumeric() or ('.' in token and token.replace('.', '', 1).isdigit()):
            print(f"number: {float(token)}")
        else:
            print(f"id: {token}")
