def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    if len(str_number) == 1:
        return number
    elif len(str_number) > 1:
        return int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))
    else:
        print("Введено некорректное число")


if __name__ == "__main__":
    print(get_multiplied_digits(402030))
