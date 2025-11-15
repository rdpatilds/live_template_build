"""Simple Python script to test Ruff setup."""


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of numbers.

    Args:
        numbers: A list of integers to sum

    Returns:
        The sum of all numbers in the list
    """
    total = 0
    for num in numbers:
        total = total + num
    return total


def greet(name: str = "World") -> str:
    """Generate a greeting message.

    Args:
        name: The name to greet

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def main():
    """Main entry point for the script."""
    print(greet("Ruff"))

    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(f"The sum of {numbers} is {result}")

    # Demonstrate some list comprehension
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")


if __name__ == "__main__":
    main()
