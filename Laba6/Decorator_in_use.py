from Decorator import weekday_only
import datetime

@weekday_only
def perform_daily_task(task_name):
    """Виконує важливе робоче завдання."""
    print(f"✅ Виконується робоче завдання: '{task_name}'")
    print(f"Дата: {datetime.date.today()}")
    return f"Завдання '{task_name}' успішно виконано."

@weekday_only
def send_work_email():
    """Симулює відправку робочого листа."""
    print("✉️ Робочий лист відправлено.")

# Тестування функцій

print("--- Тест функції 'perform_daily_task' ---")
result_task = perform_daily_task("Підготовка щотижневого звіту")
print(f"Результат виконання: {result_task}\n")
send_work_email()

# Примітка: 
# Якщо код виконується в робочий день (Пн-Пт), ви побачите "✅" та "✉️".
# Якщо код виконується у вихідний (Сб-Нд), ви побачите "⚠️" та повідомлення про заборону.