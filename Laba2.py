a = [26, 60, 20, 2, 15, 7, 999, 92, 6, 11, "банан", "апельсин", "агрус", "мандарин", "собака", "рука", "пензлик", "мишка", "шафа", "тумба"]
int_list = [i for i in a if isinstance(i, int)]
str_list = [i for i in a if isinstance(i, str)]



int_list.sort()

str_list.sort()

b = int_list + str_list
c = [i for i in int_list if i % 2 == 0]
cups = [i.upper() for i in str_list]



print("Головний список:", a)
print("Відсортований список", b)
print("Числа кратні 2:", c)
print("Список з капсом:", cups)
