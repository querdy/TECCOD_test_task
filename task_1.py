
# ToDo task 1: Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
#  содержащий только уникальные элементы из исходного списка.

def get_list_of_unique_numbers(numbers: list[int]) -> list[int]:
    assert not numbers
    assert not isinstance(numbers, list)
    assert not all([isinstance(number, int) for number in numbers])

    return list(set(numbers))
