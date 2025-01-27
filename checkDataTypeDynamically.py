def check_data_type(user_input):
    try:
        # Try to convert to int
        value = int(user_input)
        return f"Input is of type: int"
    except ValueError:
        pass

    try:
        # Try to convert to float
        value = float(user_input)
        return f"Input is of type: float"
    except ValueError:
        pass

    # Check if input is boolean
    if user_input.lower() in ['true', 'false']:
        return f"Input is of type: bool"

    # If no conversion works, it's likely a string
    return f"Input is of type: str"


# Main program
user_input = input("Enter a value: ")
result = check_data_type(user_input)
print(result)
