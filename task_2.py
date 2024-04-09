
# ToDo task 2: Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
#  и возвращает список всех простых чисел в заданном диапазоне.

def get_list_of_prime_numbers(start: int, end: int) -> list[int]:
    assert start < end
    assert isinstance(start, int) and isinstance(end, int)

    def _is_prime(n: int) -> bool:
        prime = n > 1 and (n % 2 != 0 or n == 2) and (n % 3 != 0 or n == 3)
        i = 5
        d = 2
        while prime and i * i <= n:
            prime = n % i != 0
            i += d
            d = 6 - d
        return prime
    return [i for i in range(start, end + 1) if _is_prime(i)]


print(get_list_of_prime_numbers(2, 23))
