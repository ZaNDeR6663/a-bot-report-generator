import pandas as pd

import csv
import json

# parse file.txt line by line
# find data in lines. What data?
# add this data to pd
# generate csv (or google sheets file)
# (optional) generate charts

def parse_eng():
    messages = []
    message = {'date': None,
               'trades': None,
               'profit_BTC': None,
               'profit_USDT': None,
               'avg_trade_percent': None,
               # 'day_volume': None,
               # 'portfolio_value': None,
               # 'free_BTC': None,
               }
    try:

        with open('raw_data.txt', 'r', encoding="utf8") as file:
            for line in file:
                # извлекаем дату
                text = 'Daily statistics for '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['date'] = line
                    print(line)

                # извлекаем количество сделок
                text = 'Deals made: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['trades'] = line
                    print(line)

                # profit_BTC
                text = 'BTC      | '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['profit_BTC'] = line
                    print(line)

                # profit_BTC
                text = 'USDT     | '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['profit_USDT'] = line
                    print(line)

                # Средний доход сделки:
                text = 'Average deal income: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['avg_trade_percent'] = line
                    print(line)

                # Сделок:
                text = 'Deals: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['trades_all'] = line
                    print(line)
                    messages.append(message)
                    message = {}

    except Exception as ex:
        print(ex)
    return messages


def parse_rus():
    messages = []
    message = {'date': None,
               'trades': None,
               'profit_BTC': None,
               'profit_USDT': None,
               'avg_trade_percent': None,
               # 'day_volume': None,
               # 'portfolio_value': None,
               # 'free_BTC': None,
               }
    try:
        with open('raw_data.txt', 'r', encoding="utf8") as file:
            for line in file:
                # извлекаем дату
                text = 'Статистика за '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['date'] = line
                    print(line)

                # извлекаем количество сделок
                text = 'Сделок закрыто: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['trades'] = line
                    print(line)

                # profit_BTC
                text = 'BTC    | '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['profit_BTC'] = line
                    print(line)

                # profit_BTC
                text = 'USDT   | '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['profit_USDT'] = line
                    print(line)


                # Средний доход сделки:
                text = 'Средний доход сделки: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['avg_trade_percent'] = line
                    print(line)

                # Сделок:
                text = 'Сделок: '
                num = line.find(text)
                if num != -1:
                    line = line[num:].replace(text, '').strip('\n')
                    message['trades_all'] = line
                    print(line)
                    messages.append(message)
                    message = {}

    except Exception as ex:
        print(ex)

    return messages


if __name__ == '__main__':
    msgs1 = parse_rus()
    msgs2 = parse_eng()

    with open('res_file.csv', "w", newline="", encoding='utf-8') as f1:
        fieldnames = msgs1[0].keys()
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(msgs1)
        writer.writerows(msgs2)
