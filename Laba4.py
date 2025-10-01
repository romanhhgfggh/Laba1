def main():# функція для форматування ціни
    def format_price(price: float) -> str:
        """
        Приймає число (ціну) і повертає рядок у форматі 'ціна: xxx.xx грн'
        """
        return f"ціна: {price:.2f} грн"
    
    
    # функція для перевірки наявності товарів
    def check_availability(*items, store: dict) -> dict:
        """
        Приймає довільну кількість товарів (імена рядками)
        та словник магазину {товар: (ціна, наявність)}
        Повертає словник {товар: True/False}
        """
        return {item: (item in store and store[item][1]) for item in items}
    
    
    # функція для обробки замовлення
    def process_order(order: list, store: dict, action: str):
        """
        order: список замовлених товарів
        store: словник {товар: (ціна, наявність)}
        action: 'buy' або 'price'
        """
        # перевіряємо наявність
        availability = check_availability(*order, store=store)
    
        # якщо хоча б один товар відсутній — замовлення неможливе
        if not all(availability.values()):
            print("❌ Деякі товари відсутні в магазині!")
            print("Наявність:", availability)
            return
    
        # всі товари є
        total = sum(store[item][0] for item in order)
    
        if action == "price":
            print("Вартість замовлення:")
            for item in order:
                print(f"{item} — {format_price(store[item][0])}")
            print("Загалом:", format_price(total))
    
        elif action == "buy":
            print("✅ Замовлення підтверджено!")
            print("До сплати:", format_price(total))
        else:
            print("Невідома дія! Використовуйте 'buy' або 'price'.")
    
    
    # ================================
    # Приклад використання
    store = {
        "хліб": (25.5, True),
        "молоко": (38.0, True),
        "яйця": (52.3, False),
        "сир": (120.0, True)
    }
    
    # Користувач вибрав замовлення

    order = ["хліб", "молоко"]
    
    # 1) Переглянути ціну
    process_order(order, store, "price")
if __name__ == "__main__":
    main()
