import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # We only need to check up to the square root because if a number 'n' has a divisor
    # greater than its square root, it must also have a divisor smaller than its square root.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

# Example Usage:
num_to_check = int(input("Enter a number: "))

if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")