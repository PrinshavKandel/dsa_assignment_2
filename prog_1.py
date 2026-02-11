def is_balanced(expression):
    """
    Check if a mathematical expression has balanced parentheses using a stack.
    Returns True if balanced, False otherwise.
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Define matching pairs
    opening = '({['
    closing = ')}]'
    matches = {')': '(', '}': '{', ']': '['}
    
    # Process each character in the expression
    for char in expression:
        if char in opening:
            # Push opening parenthesis onto stack
            stack.append(char)
        elif char in closing:
            # Check if there's a matching opening parenthesis
            if not stack or stack[-1] != matches[char]:
                return False
            # Pop the matching opening parenthesis
            stack.pop()
    
    # Expression is balanced if stack is empty
    return len(stack) == 0


# Test the program with the given expressions
test_expressions = [
    "a + (b - c) * (d",
    "m + [a - b * (c + d * {m})]",
    "a + (b - c)"
]

print("Checking balanced parentheses:\n")
for expr in test_expressions:
    result = is_balanced(expr)
    status = "Balanced" if result else "Not Balanced"
    print(f"Expression: {expr}")
    print(f"Result: {status}\n")
