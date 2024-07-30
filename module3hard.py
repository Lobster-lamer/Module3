def len_is_not_zero(list_element) -> bool:
    if '__len__' in dir(list_element):
        return len(list_element) > 0
    else:
        return False


def sum_all_digits_of_list(list_to_find_digits: list) -> int:
    elements_sum = 0
    for list_element in list_to_find_digits:
        if isinstance(list_element, int):
            elements_sum += list_element
        elif isinstance(list_element, str):
            elements_sum += len(list_element)
        elif len_is_not_zero(list_element):
            if isinstance(list_element, dict):
                elements_sum += sum_all_digits_of_list(list(list_element.items()))
            else:
                elements_sum += sum_all_digits_of_list(list_element)
    return elements_sum


if __name__ == "__main__":
    data_structure = [
      [1, 2, 3],
      {'a': 4, 'b': 5},
      (6, {'cube': 7, 'drum': 8}),
      "Hello",
      ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    print(sum_all_digits_of_list(data_structure))
