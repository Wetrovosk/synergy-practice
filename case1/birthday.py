from datetime import date
import calendar

# Шаблоны цифр и пробела
DIGIT_PATTERNS = {
    '0': [
        "***",
        "* *",
        "* *",
        "* *",
        "***"
    ],
    '1': [
        "  *",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    '2': [
        "***",
        "  *",
        "***",
        "*  ",
        "***"
    ],
    '3': [
        "***",
        "  *",
        "***",
        "  *",
        "***"
    ],
    '4': [
        "* *",
        "* *",
        "***",
        "  *",
        "  *"
    ],
    '5': [
        "***",
        "*  ",
        "***",
        "  *",
        "***"
    ],
    '6': [
        "***",
        "*  ",
        "***",
        "* *",
        "***"
    ],
    '7': [
        "***",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    '8': [
        "***",
        "* *",
        "***",
        "* *",
        "***"
    ],
    '9': [
        "***",
        "* *",
        "***",
        "  *",
        "***"
    ],
    ' ': [
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ]
}

 # день недели
def get_weekday(birth_date: date) -> str:
    days = [
        "Понедельник", "Вторник", "Среда", 
        "Четверг", "Пятница", "Суббота", "Воскресенье"
    ]
    return days[birth_date.weekday()]

# високосный год
def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

# возраст
def calculate_age(birth_date: date) -> int:
    today = date.today()
    # минус 1, если в этом году дня рождения еще не было
    has_birthday_passed = (today.month, today.day) >= (birth_date.month, birth_date.day)
    return today.year - birth_date.year - (not has_birthday_passed)

# электронное табло
def print_banner_date(birth_date: date) -> None:
    formatted_str = birth_date.strftime("%d %m %Y")
    for row in range(5):
        line = []
        for char in formatted_str:
            pattern = DIGIT_PATTERNS.get(char, DIGIT_PATTERNS[' '])
            line.append(pattern[row])
        print(" ".join(line))


def main():
    print("=== Ваша дата рождения ===")
    try:
        day = int(input("Введите число дня рождения (1-31): "))
        month = int(input("Введите месяц рождения (1-12): "))
        year = int(input("Введите год рождения (например, 1995): "))
        
        birth_date = date(year, month, day)
    except ValueError as e:
        print(f"Ошибка! Проверьте правильность введенных чисел ({e}).")
        return

    # расчет данных
    weekday = get_weekday(birth_date)
    leap = is_leap_year(year)
    age = calculate_age(birth_date)

    # вывод данных
    print("\n=== Результаты ===")
    print(f"День недели: {weekday}")
    print(f"Високосный год: {'Да' if leap else 'Нет'}")
    print(f"Полных лет: {age}")

    # табло
    print("\n=== Дата рождения (электронное табло) ===")
    print_banner_date(birth_date)


if __name__ == "__main__":
    main()