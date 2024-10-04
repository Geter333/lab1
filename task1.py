# Функція для перевірки введеного числа
def validate_input(value):
    return 1 <= value <= 100

# Функція для обчислення значення X
def calculate_x(a, b):
    if a > b:
        x = a + b
    elif a == b:
        x = a * b
    else:
        x = b - a
    return x

# Основна частина програми
def main():
    try:
        # Введення значень a та b користувачем
        a = int(input("Введіть значення a (від 1 до 100): "))
        b = int(input("Введіть значення b (від 1 до 100): "))

        # Перевірка введених значень
        if not (validate_input(a) and validate_input(b)):
            print("Помилка: значення повинні бути в діапазоні від 1 до 100.")
            return

        # Обчислення X
        x = calculate_x(a, b)

        # Виведення результату
        print(f"Значення X: {x}")

    except ValueError:
        print("Помилка: введені значення повинні бути цілими числами.")

# Виклик основної функції
if __name__ == "__main__":
    main()
