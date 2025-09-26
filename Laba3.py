def main():
    students = {}  # словник: ім'я -> оцінка

    while True:
        name = input("Введіть ім'я студента: ")
        if name.lower() == "stop":
            break

        try:
            grade = int(input(f"Введіть оцінку для учня {name}: "))
            if grade < 1 or grade > 12:
                print("Оцінка має бути від 1 до 12!")
                continue
            students[name] = grade
        except ValueError:
            print("Потрібно ввести ціле число!")
            continue

    print("\n=== Результати ===")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    if students:
        avg = sum(students.values()) / len(students)
        print(f"\nСередній бал по групі: {avg:.2f}")

        awesome = [n for n, g in students.items() if 10 <= g <= 12]
        good = [n for n, g in students.items() if 7 <= g <= 9]
        ok = [n for n, g in students.items() if 4 <= g <= 6]
        bad = [n for n, g in students.items() if 1 <= g <= 3]

        print(f"Кількість відмінників (10-12): {len( awesome)} { awesome}")
        print(f"Кількість хорошистів (7-9): {len(good )} {good }")
        print(f"Кількість відстаючих (4-6): {len(ok)} {ok}")
        print(f"Кількість тих, хто не здав (1-3): {len(bad)} {bad}")
    else:
        print("Немає введених даних.")

if __name__ == "__main__":
    main()
