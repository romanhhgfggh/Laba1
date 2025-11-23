import random

def create_test_file(filename="laba9_text.txt", lines=105, chars_per_line=110):
    # Використовуємо кирилицю та пробіли для імітації слів
    ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя      " 
    
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(lines):
            # Генеруємо рядок із 110 символів
            line = "".join(random.choice(ukr_alphabet) for _ in range(chars_per_line))
            # Прибираємо зайві пробіли на початку/кінці та додаємо перенос
            f.write(line.strip() + "\n")
    
    print(f"Файл '{filename}' успішно створено.")

# Запуск створення файлу
create_test_file()
