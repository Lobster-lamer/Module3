from consoleTextStyle import ConsoleTextStyle as CoTeSt


def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(checking_string: str,
                in_list: list) -> bool:
    count_calls()
    for member_number in range(len(in_list)):
        if isinstance(in_list[member_number], str):
            in_list[member_number].lower()
    return checking_string.lower() in in_list


if __name__ == "__main__":
    calls = 0
    while 1:
        string_to_info = input("Введите строку, пж (Шоб выйти из цикла, \033[9mзаймитесь собой"
                               "\033[0m напишите \033[1mБАНАН\033[0m):")
        if "БАНАН" in string_to_info:
            break
        string_to_info = string_info(string_to_info)
        print(string_to_info)
        print("Yeeeeeah, bitches!" if is_contains("bitch", list(string_to_info)) else "No bitches?")
    print(f"\n{CoTeSt.Color.YELLOW}Всего было вызвано функций:{CoTeSt.Color.PURPLE}{calls}{CoTeSt.Color.YELLOW} \n"
          f"От так уот")
