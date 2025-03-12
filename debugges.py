def is_narc(n):
    """Check if a number is narcissistic."""
    
    # Convert the number to a string to easily access individual digits
    num_str = str(n)
    
    # Calculate the number of digits in the number
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    # CHANGED: Replaced '*' with '**' for exponentiation
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == n


def print_narc_numbers(start, end):
    """Print all narcissistic numbers in a given range."""
    
    # Iterate through the range from start to end (inclusive)
    for num in range(start, end + 1):
        
        # Check if the number is narcissistic using the is_narc function
        # CHANGED: Corrected function name from 'is_narcissistic' to 'is_narc'
        if is_narc(num):
            print(num)


# Call the function to print narcissistic numbers between 1000 and 5000
# CHANGED: Corrected function name from 'print_narcis_numbers' to 'print_narc_numbers'
print_narc_numbers(1000, 5000)
