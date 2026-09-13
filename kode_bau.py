"""Module to demonstrate clean Python code passing Pylint quality checks."""


def calculate_sum(first_val, second_val, numbers_list, offset):
    """Calculate the sum of clean input numbers.

    :param first_val: First integer component.
    :param second_val: Second integer component.
    :param numbers_list: List containing numerical values.
    :param offset: Numerical offset to add.
    :return: Total calculated sum or None.
    """
    total = 0

    if first_val and not second_val:
        first_item = numbers_list[0] if numbers_list else 0
        total = first_item + offset + 1

    return total


if __name__ == "__main__":
    calculate_sum(1, 2, [2], 3)
