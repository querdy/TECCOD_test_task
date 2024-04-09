# ToDo task 4: Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию


def sorted_words_generator(words: list[str]):
    assert isinstance(words, list)
    assert all([isinstance(word, str) for word in words])
    yield sorted(words, key=len)
    yield sorted(words, key=len, reverse=True)


if __name__ == "__main__":
    test_list_of_string = ("Написать программу, которая сортирует список строк по длине, "
                           "сначала по возрастанию, а затем по убыванию").split(" ")
    generator = sorted_words_generator(test_list_of_string)

    print(f"Исходный список строк: {test_list_of_string}")
    print(f"Отсортировано по увеличению длины: {generator.__next__()}")
    print(f"Отсортировано по уменьшению длины: {generator.__next__()}")
