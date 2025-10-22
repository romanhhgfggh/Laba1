import datetime
import functools

def weekday_only(func):
    """
    Декоратор, який дозволяє викликати функцію 
    тільки у робочі дні (з понеділка по п'ятницю).
    Повертає None та виводить повідомлення, якщо сьогодні вихідний.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Отримання поточного дня тижня
        # datetime.date.today().weekday() повертає:
        # 0 = Понеділок, 1 = Вівторок, ..., 4 = П'ятниця, 5 = Субота, 6 = Неділя
        today = datetime.date.today().weekday()
        
        # Робочі дні - це дні з індексами від 0 до 4
        if 0 <= today <= 4:
            # Сьогодні робочий день, викликаємо оригінальну функцію
            return func(*args, **kwargs)
        else:
            # Сьогодні вихідний (Субота або Неділя)
            day_name = datetime.date.today().strftime('%A')
            print(f"⚠️ Виклик функції '{func.__name__}' заборонено.")
            print(f"Сьогодні {day_name} – вихідний день.")
            return None  # Повертаємо None або можна було б згенерувати виключення

    return wrapper

# Приклад, якщо б ви хотіли протестувати його прямо тут:
# @weekday_only
# def greet():
#     print("Привіт! Сьогодні робочий день, можемо працювати!")

# greet()