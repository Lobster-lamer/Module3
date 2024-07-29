from consoleTextStyle import ConsoleTextStyle as CoTeSt


def print_params(first=1,
                 second="строка",
                 third=True,
                 *args) -> None:
    print(first, second, third, *args)


if __name__ == "__main__":
    # 1.Функция с параметрами по умолчанию:
    CoTeSt.colorful_text("1.Функция с параметрами по умолчанию:", CoTeSt.Color.CYAN)
    listik = []
    print_params()
    for value in range(3):
        listik.append(value+1)
        print_params(*listik)
    print_params(second = 25)
    print_params(third = list(x+1 for x in range(3)))

    # 2.Распаковка параметров:
    CoTeSt.colorful_text("\n2.Распаковка параметров", CoTeSt.Color.CYAN)
    values_list = [0, "Ноль", False]
    values_dict = {"first": 1,
                   "second": "Один",
                   "third": True}
    print_params(*values_list)
    print_params(**values_dict)

    # 3.Распаковка + отдельные параметры:
    CoTeSt.colorful_text("\n3.Распаковка + отдельные параметры", CoTeSt.Color.CYAN)
    values_list2 = [2, "Два"]
    print_params(*values_list2, 42)
