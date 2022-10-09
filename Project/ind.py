#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_plane():
    """
    Запросить данные о самолете.
    """
    destination = input("Пункт назначения: ")
    num = input("Номер рейса: ")
    typ = input("Тип самолета: ")

    # Создать словарь.
    return {
        'destination': destination,
        'num': num,
        'typ': typ,
    }


def display_planes(staff):
    """
    Отобразить список самолетов.
    """
    # Проверить, что список самолетов не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолета"
            )
        )
        print(line)

        # Вывести данные о всех самолетах.
        for idx, plane in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    plane.get('destination', ''),
                    plane.get('num', 0),
                    plane.get('typ', '')
                )
            )

        print(line)

    else:
        print("Список самолетов пуст")


def select_planes(staff, jet):
    """
    Выбрать самолеты с заданным типом.
    """
    # Сформировать список самолетов.
    result = []
    for plane in staff:
        if jet == plane.get('typ', ''):
            result.append(plane)

    # Возвратить список выбранных самолетов.
    return result


def main():
    """
    Главная функция программы.
    """
    # Список самолетов.
    planes = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о самолете.
            plane = get_plane()

            # Добавить словарь в список.
            planes.append(plane)
            # Отсортировать список в случае необходимости.
            if len(planes) > 1:
                planes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            # Отобразить все самолеты.
            display_planes(planes)

        elif command.startswith('select '):
            # Разбить команду на части для выделения пункта назначения.
            part = command.split(' ', maxsplit=1)
            com = part[1]

            # Выбрать самолеты заданного типа
            selected = select_planes(planes, com)
            # Отобразить выбранные самолеты
            display_planes(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить самолет;")
            print("list - вывести список самолетов;")
            print("select <тип> - запросить самолеты заданного типа;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()