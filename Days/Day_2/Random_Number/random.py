import datetime

def generate_random_number(max_number):
    def perform_operation(x):
        operation_digit = x % 4
        number_to_operate = x % 10 + 1  # Ensuring non-zero

        result = 0

        if operation_digit == 0:  # integer division
            result = x // number_to_operate
        elif operation_digit == 1:  # multiply
            result = x * number_to_operate
        elif operation_digit == 2:  # add
            result = x + number_to_operate
        elif operation_digit == 3:  # subtract
            result = x - number_to_operate

        # Convert negative result to positive
        return abs(result)

    result = 0
    while result == 0 or result > max_number:
        current_time = datetime.datetime.now()
        x = current_time.microsecond % 100  # Using microseconds for more variability

        result = perform_operation(x)
        # Scale down the result to be within 1 to max_number
        result = result % max_number + 1

    return result

# Example usage
max_number = 6
random_number = generate_random_number(max_number)
print(f"Generated random number (1-{max_number}):", random_number)
