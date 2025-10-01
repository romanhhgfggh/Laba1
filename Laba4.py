store = {
    'гречка': 15.85,
    'хліб': 25,
    'мясо': 321,
    'молоко': 38,
    'цибуля': 99.9,
    'херсонський кавунчик': 18,
    'сало': 232,
    'буряк': 65
}


def format_price(price):
    return f"ціна: {price:.2f} ГРН"


def check(products):
    result = {}
    for product in products:
        result[product] = product in store
    return result


def order(products):
    availability = check(products)

    if all(availability.values()):
        total = 0
        for product in products:
            total += store[product]
        return f"Усі товари є! Загальна {format_price(total)}"
    else:
        miss = [product for product, available in availability.items()
                if not available]
        return f"Немає в наявності: {' '.join(miss)}"



  

def main():
    while True:
        print("1 - Переглянути ціну\n2 - Купити")
        choice = input("Ваш вибір: ")

        user_input = input("Введіть товари через пробіл: ")
        products = user_input.split()

        if choice == "1":
            availability = check(products)
            for product, is_available in availability.items():
                if is_available:
                    print(f"{product} – {format_price(store[product])}")
                else:
                    print(f"{product} – Немає в наявності")

        elif choice == "2":
            print(order(products))
        else:
            print("Невірний вибір, спробуй ще раз.")



    process_order(order, store, "price")
if __name__ == "__main__":
    main()
