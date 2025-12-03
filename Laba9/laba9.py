def pair_counter_generator(filepath, target_pairs):
    """
    Генератор, який читає файл пострічково і рахує кількість входжень
    заданих пар букв ВИКЛЮЧНО всередині слів.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                # Ініціалізуємо лічильник для поточного рядка
                line_stats = {pair: 0 for pair in target_pairs}
                
                # Розбиваємо рядок на слова (це гарантує, що ми не рахуємо пари між словами)
                words = line.split()
                
                for word in words:
                    # Перевіряємо пари тільки всередині слова
                    # range(len(word) - 1) гарантує, що ми не вийдемо за межі слова
                    for i in range(len(word) - 1):
                        current_pair = word[i:i+2].lower() # беремо зріз з 2 букв
                        
                        if current_pair in line_stats:
                            line_stats[current_pair] += 1
                
                # Yield повертає результат для кожного рядка окремо (ліниве обчислення)
                yield line_number, line_stats

    except FileNotFoundError:
        print("Помилка: Файл не знайдено. Спочатку запустіть скрипт створення файлу.")

# --- Використання ---

# Пари для пошуку (як у вашому прикладі)
targets = ['ан', 'ун', 'ну']


# Створюємо об'єкт генератора
gen = pair_counter_generator("laba9_text.txt", targets)

# Ітеруємося по генератору
total_counts = {pair: 0 for pair in targets}

for line_num, stats in gen:
    # Виводимо статистику тільки якщо в рядку щось знайшли (для чистоти виводу)
    if sum(stats.values()) > 0:
        print(f"Рядок {line_num}: {stats}")
    
    # Додаємо до загальної суми
    for pair in targets:
        total_counts[pair] += stats[pair]

print("-" * 30)
print(f"Загальний результат по тексту: {total_counts}")
