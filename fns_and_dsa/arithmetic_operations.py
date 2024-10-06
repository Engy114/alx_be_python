def perform_operation(num1, num2, operation):
    """
    Perform the specified arithmetic operation.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (string): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation, or a message if invalid operation or division by zero.
    """
    # Perform the arithmetic operation based on the 'operation' parameter
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            # Check for division by zero
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation."
