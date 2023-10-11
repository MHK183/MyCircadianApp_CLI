import os
from datetime import datetime

from logo import intro
from circadian_rhythm import CircadianRhythm

EXAMPLE = datetime.today().strftime("%Y%m%d")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def validate_date(date):
    try:
        if len(date) != 8 or not date.isdigit():
            raise ValueError(f"올바른 날짜 형식이 아닙니다. (예: {EXAMPLE})")
        return True
    except ValueError as e:
        print(e)
        return False


def insert_or_delete():
    user_input1 = input("삽입 또는 수정 'e', 삭제하기 'd' : ").lower()
    if user_input1 == 'e' or user_input1 == 'd':
        return user_input1
    else:
        return insert_or_delete()


def main():
    clear_screen()
    # intro logo
    print(intro)
    is_on = True
    while is_on:
        input_date = input(f"날짜를 입력하세요 (예: {EXAMPLE}): ")
        if validate_date(input_date):
            circadian_rhythm = CircadianRhythm(input_date)

            user_select = insert_or_delete()
            if user_select == 'e':
                circadian_rhythm.insert()
            elif user_select == 'd':
                circadian_rhythm.delete()

            if input("계속해서 입력하기 'y', or 종료하기 '아무 키나 입력' : ").lower() == 'y':
                return main()
            else:
                is_on = False


if __name__ == '__main__':
    main()