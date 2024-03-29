# 2. Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку
# Техническое задание:
#
# Список может содержать произвольное кол-во элементов. Его элементы - строки.
# Пример исходного списка: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Строки-элементы списка:
# могут содержать цифры, обозначающие часы/минуты/секунды: "1" "12" "55"; одна или две цифры, без привязки к ограничениям
# на 60 минут/секунд и 24 часа. Т.е. '79', 'минут' - это корректно.
# могут начинаться со знаков + или - и обозначают температуры: "+5", "-7"; любое целое число. В начале может быть знак
# плюс или минус, но может и не быть.
# могут быть просто символьными строками: слова в начале и конце строк-чисел пробелов нет.
# строки-числа и строки-слова не обязательно идут точно через один.
# Обработка списка:
# обособить каждое целое число кавычками (добавить строку-кавычку до и после элемента списка, являющегося числом)
# дополнить это число нулём до двух целочисленных разрядов
# Например исходный список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'].
# Тогда результирующий список: ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов'].
# Обработанный список вывести на экран
# Сформировать из обработанного списка строку, соединив все элементы
# Для примера выше: 'в "05" часов "17" минут температура воздуха была "+05" градусов'
# Вывести строку на экран.
# Обратите внимание на отсутствие "лишних" пробелов около кавычек, например '"08" минут' - правильно, а '" 08 " минут' - неправильно.
# Формат вывода результата:
# Исходный, результирующий список и строку выводим на экран через print.
#
# Примеры/Тесты:
# Исходный список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Новый список + добавление элементов-кавычек:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Исходный список:
# ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
# Новый список + добавление элементов-кавычек:
# ['примерно в', '"', '23', '"', 'часа', '"', '08', '"', 'минут', '"', '03', '"', 'секунд', 'температура', 'воздуха', 'была', '"', '-05', '"', 'градусов Цельсия', 'темп', 'воды', '"', '+12', '"', 'градусов', 'Цельсия']
#
# Примечание:
#
# Регулярные выражения не используем. Учимся парсить строку самостоятельно.
# Алгоритм
#
# Сколько проходов по списку вам понадобится? Достаточно одного прохода.
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Это первый шаг - парсить строку-число и добавлять нули по необходимости.
# Задание упрощенное
#
# Если у вас не получается добавить правильно элементы-кавычки - упростим задачу. Обработайте строки-числа в соответствии с
# условием задачи и вставьте кавычки прямо в эту же строку. Т.е. вы меняете элементы списка, не добавляя новых элементов.
# Задание повышенной сложности (задание со звездочкой)
#
# Не создавайте новый список. Это называется решить «in place». Измените существующий список, добавив элементы-кавычки в
# соответствии с условием задачи. Не добавляйте «лишних» элементов - только элементы-кавычки и не удаляйте из списка никаких
# элементов. Эта задача намного серьезнее, чем может сначала показаться.

# lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# #  ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# # в "05" часов "17" минут температура воздуха была "+05" градусов
# new_lst = []
# i = 0
# a = '"'
# x = ''
# st = ''
# while i < len(lst):
#     if lst[i].isdigit() and len(lst[i]) == 1:
#         new_lst.extend([a, '0' + lst[i], a])
#     elif lst[i].isdigit():
#         new_lst.extend([a, lst[i], a])
#     elif not lst[i].isdigit():
#
#         for symbol in lst[i]:
#             x += symbol
#
#             if symbol.isdigit():
#
#                 lst[i] = x[-2] + '0' + symbol
#
#                 new_lst.extend([a, lst[i], a])
#         new_lst.append(lst[i])
#
#     i += 1
#
# print(lst)
# print(new_lst)

weather_forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_weather_forecast = []
out_weather_forecast = ''
a = '"'
for i in weather_forecast:
    if i.isalpha():
        new_weather_forecast.extend([i])
    elif i.isdigit() and len(i) > 1:
        new_weather_forecast.extend([a, i, a])
    elif i.isdigit():
        new_weather_forecast.extend([a, '0' + i, a])
    else:
        new_weather_forecast.extend([a, i[0] + '0' + i[1:], a])
    if i.isalpha():
        out_weather_forecast += str(i) + ' '
    else:
        out_weather_forecast += str(new_weather_forecast[-3]) + str(new_weather_forecast[-2]) + str(
            new_weather_forecast[-1]) + ' '

print(weather_forecast)
print(new_weather_forecast)
print(out_weather_forecast)


