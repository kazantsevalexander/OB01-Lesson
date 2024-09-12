class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {} #словарь, где ключ - название товара, а значение - его цена.
                            # Например, `{'apples': 0.5, 'bananas': 0.75}`.

    def add_prod(self, name_prod, price_prod): #-  метод для добавления товара в ассортимент.
        self.items[name_prod] = price_prod
        print(f"Товар: {name_prod} добавлен по цене {price_prod} в магазин {self.name}")

    def del_prod(self, name_prod): #метод для удаления товара из ассортимента.
        if name_prod in self.items:
            del self.items[name_prod]
            print(f"Товар: {name_prod} удален из ассортимента")
        else:
            print(f"Товар '{name_prod}' не найден в ассортименте.")

    def get_price_prod(self, name_prod): #метод для получения цены товара по его названию.
                                # Если товар отсутствует, возвращайте None.
        if name_prod in self.items:
            price = self.items.get(name_prod)
            print(f"Товар '{name_prod}' доступен по цене {price}")
        else:
            print(f"Товар '{name_prod}' не найден в ассортименте.")

    def update_price_prod(self, name_prod, new_price): #метод для обновления цены товара.
        if name_prod in self.items:
            self.items[name_prod] = new_price
            print(f"Товар '{name_prod}' теперь доступен по цене {new_price}")

# Markets
market1 = Store("Green", "г.Минск, ул. Притыцкого, 51")
market2 = Store("Евроопт", "г.Гомель, ул. Гагарина, 23")
market3 = Store("БелМаркет", "г.Брест, ул. Варшавское шоссе, 17")
market4 = Store("Соседи", "г.Могилёв, ул. Ботаническая, 9")
market5 = Store("Виталюр", "г.Витебск, ул. Чкалова, 45")
market6 = Store("Рублёвский", "г.Гродно, ул. Карского, 12")

# market1 - Green
market1.add_prod("Хлеб Беларусь", "1.2 руб.")
market1.add_prod("Квас 'Друць'", "0.9 руб.")
market1.add_prod("Квас 'Славутич'", "1.0 руб.")
market1.add_prod("Гречневая крупа", "2.2 руб.")
market1.add_prod("Мёд дикий", "4.5 руб.")
market1.add_prod("Сыр 'Витебский'", "5.3 руб.")
market1.add_prod("Квас 'Кривич'", "0.95 руб.")
market1.add_prod("Пшённая каша", "1.6 руб.")
market1.add_prod("Бочковой огурец", "1.7 руб.")

# market2 - Евроопт
market2.add_prod("Хлеб 'Чорны бор'", "1.4 руб.")
market2.add_prod("Печеная рыба", "6.1 руб.")
market2.add_prod("Квас 'Друць'", "0.9 руб.")
market2.add_prod("Сыр козий 'Белогорский'", "5.7 руб.")
market2.add_prod("Льняное масло", "3.8 руб.")
market2.add_prod("Медовуха 'Полесье'", "6.7 руб.")
market2.add_prod("Пшённая каша", "1.6 руб.")
market2.add_prod("Яблоки сушеные", "2.5 руб.")
market2.add_prod("Гречневая крупа", "2.2 руб.")

# market3 - БелМаркет
market3.add_prod("Каша ячневая", "1.5 руб.")
market3.add_prod("Пирог с медом", "3.2 руб.")
market3.add_prod("Квас 'Славутич'", "1.0 руб.")
market3.add_prod("Гречневая мука", "2.4 руб.")
market3.add_prod("Сушеная свинина", "7.3 руб.")
market3.add_prod("Сыр козий 'Белогорский'", "5.7 руб.")
market3.add_prod("Бочковой огурец", "1.7 руб.")
market3.add_prod("Квас 'Кривич'", "0.95 руб.")
market3.add_prod("Гречневая крупа", "2.2 руб.")

# market4 - Соседи
market4.add_prod("Сало копченое", "6.3 руб.")
market4.add_prod("Медовый напиток", "5.8 руб.")
market4.add_prod("Хлеб 'Друцк'", "1.2 руб.")
market4.add_prod("Медовуха 'Старажытная'", "7.2 руб.")
market4.add_prod("Льняное масло", "3.8 руб.")
market4.add_prod("Яблоки сушеные", "2.5 руб.")
market4.add_prod("Сыр 'Витебский'", "5.3 руб.")
market4.add_prod("Сыр с травами", "4.9 руб.")
market4.add_prod("Пшённая каша", "1.6 руб.")

# market5 - Виталюр
market5.add_prod("Яблоки сушеные", "2.5 руб.")
market5.add_prod("Сушеный лён", "4.4 руб.")
market5.add_prod("Сыр 'Витебский'", "5.3 руб.")
market5.add_prod("Медовуха 'Полесье'", "6.7 руб.")
market5.add_prod("Хлеб 'Каменецкий'", "1.3 руб.")
market5.add_prod("Гречневая мука", "2.4 руб.")
market5.add_prod("Квас 'Княжич'", "0.85 руб.")

while True:
    print("\nВыберите действие для тестирования магазина 'Виталюр':")
    print("1. Добавить товар")
    print("2. Удалить товар")
    print("3. Получить цену товара")
    print("4. Обновить цену товара")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        name_prod = input("Введите название товара: ")
        price_prod = input("Введите цену товара: ")
        market5.add_prod(name_prod, price_prod)
    elif choice == '2':
        name_prod = input("Введите название товара для удаления: ")
        market5.del_prod(name_prod)
    elif choice == '3':
        name_prod = input("Введите название товара для получения цены: ")
        market5.get_price_prod(name_prod)
    elif choice == '4':
        name_prod = input("Введите название товара для обновления цены: ")
        new_price = input("Введите новую цену товара: ")
        market5.update_price_prod(name_prod, new_price)
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
