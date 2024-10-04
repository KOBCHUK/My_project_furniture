from furniture.my_furniture import required_materials, calculate_volume, calculate_weight, calculate_surface_area, \
    generate_report


def display_menu():
    """Відображає меню користувача."""
    print("\n--- Меню ---")
    print("1. Розрахунок необхідних матеріалів для виробу")
    print("2. Розрахунок об'єму виробу")
    print("3. Розрахунок ваги виробу")
    print("4. Розрахунок площі поверхні виробу")
    print("5. Розрахунок вартості виробництва")
    print("6. Вийти")


def main():
    while True:
        display_menu()
        choice = input("Виберіть опцію (1-6): ")

        if choice == '1':
            product = input("Введіть назву виробу (шафа, стіл, стілець): ")
            materials_needed = required_materials(product)
            print(f"Необхідні матеріали для {product}: {materials_needed}")

        elif choice == '2':
            product = input("Введіть назву виробу (шафа, стіл, стілець): ")
            volume = calculate_volume(product)
            print(f"Об'єм {product}: {volume} м³")

        elif choice == '3':
            product = input("Введіть назву виробу (шафа, стіл, стілець): ")
            weight = calculate_weight(product)
            print(f"Вага {product}: {weight} кг")

        elif choice == '4':
            product = input("Введіть назву виробу (шафа, стіл, стілець): ")
            surface_area = calculate_surface_area(product)
            print(f"Площа поверхні {product}: {surface_area} м²")

        elif choice == '5':
            product = input("Введіть назву виробу (шафа, стіл, стілець): ")
            total_cost = generate_report(product)
            print(total_cost)

        elif choice == '6':
            print("Дякуємо за використання програми!")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()