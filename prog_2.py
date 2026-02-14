def infix_to_postfix(expression):

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Stack for operators
    stack = []
    # Result postfix expression
    postfix = []
    
    # Process each token in the expression
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # Skip whitespace
        if char == ' ':
            i += 1
            continue
        
        # If character is operand (digit or multi-digit number)
        if char.isdigit() or char == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            postfix.append(num)
            continue
        
        # If character is opening parenthesis
        elif char == '(':
            stack.append(char)
        
        # If character is closing parenthesis
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        
        # If character is an operator
        elif char in precedence:
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
        
        i += 1
    
    # Pop remaining operators from stack
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)


def evaluate_postfix(postfix):
    
    # Stack for operands
    stack = []
    
    # Split postfix expression into tokens
    tokens = postfix.split()
    
    for token in tokens:
        # If token is a number, push to stack
        if token.replace('.', '').replace('-', '').isdigit():
            stack.append(float(token))
        
        # If token is an operator, pop two operands and apply operation
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
            else:
                raise ValueError(f"Unknown operator: {token}")
            
            stack.append(result)
    
    # Final result should be the only element in stack
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]


def convert_and_evaluate(infix):
    
    print(f"Infix Expression: {infix}")
    
    # Convert to postfix
    postfix = infix_to_postfix(infix)
    print(f"Postfix Expression: {postfix}")
    
    # Evaluate postfix
    result = evaluate_postfix(postfix)
    print(f"Result: {result}")
    print("-" * 50)
    
    return result


# Test the program with various expressions
if __name__ == "__main__":
    print("INFIX TO POSTFIX CONVERTER AND EVALUATOR\n")
    print("=" * 50)
    
    test_expressions = [
        "3 + 5 * 2",
        "(3 + 5) * 2",
        "10 + 2 * 6",
        "100 * 2 + 12",
        "100 * (2 + 12)",
        "5 + ((1 + 2) * 4) - 3",
        "10 / 2 + 3 * 4",
        "2 ^ 3 + 5"
    ]
    
    for expr in test_expressions:
        try:
            convert_and_evaluate(expr)
        except Exception as e:
            print(f"Error: {e}")
            print("-" * 50)
