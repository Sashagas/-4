import json


def task() -> float:
    # Чтение из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений
    total = sum(item['score'] * item['weight'] for item in data)

    # Возвращаем результат, округленный до 3 знаков после запятой
    return round(total, 3)


# Выводим результат
print(task())
