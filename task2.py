# Функція для обчислення суми ряду S
def calculate_sum_and_count(n):
    total_sum = 0.0  # Початкова сума
    count = 0  # Лічильник елементів

    for i in range(1, n + 1):
        total_sum += 1 / i  # Додаємо член ряду
        count += 1  # Збільшуємо лічильник

    return total_sum, count

# Основна частина програми
def main():
    N = 30  # Задане число N

    # Обчислюємо суму та кількість членів ряду
    total_sum, count = calculate_sum_and_count(N)

    # Виведення результатів
    print(f"Сума ряду S: {total_sum}")
    print(f"Кількість членів ряду: {count}")

# Виклик основної функції
if __name__ == "__main__":
    main()
