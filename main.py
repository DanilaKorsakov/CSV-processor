import csv
from tabulate import tabulate
import argparse


def isNumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    

def get_filter_values(filter):

    filters = ['>','<','=']
    rigth_filter = False
    filter_symb = ''

    for symbol in filter:
        if symbol in filters:
            filter_symb = symbol
            rigth_filter = True

    if rigth_filter:
        column, value = filter.split(filter_symb)
        return column, value, filter_symb
    else:
        return '','',''


def get_aggregate_values(aggregate):

    aggregates = ['min','max','avg']
    column, value = aggregate.split('=')
    if value in aggregates:
        return column, value
    else:
        return '',''
    

def get_filtered_products(products, column, value, filter_symb):
    filtered_products = []

    if filter_symb == '>':
        filtered_products = [product for product in products if float(product[column])>float(value)]

    if filter_symb == '<':
        filtered_products = [product for product in products if float(product[column])<float(value)]        

    if filter_symb == '=':
        if isNumber(value):
            filtered_products = [product for product in products if float(product[column])==float(value)]
        else:
            filtered_products = [product for product in products if product[column]==value]

    return filtered_products


def get_aggregation_result(products, column, value):
    aggregation = {}
    if value == 'min':
        aggregation = min(products, key=lambda x: float(x[column]))
        aggregation = [aggregation[column]]
    if value == 'max':
        aggregation = max(products, key=lambda x: float(x[column]))
        aggregation = [aggregation[column]]
    if value == 'avg':
        products_values = [float(product[column]) for product in products]
        aggregation = [sum(products_values)/len(products_values)]

    return aggregation


def main():

    parser = argparse.ArgumentParser(description='Фльтрация данных продуктов(цена, рейтинг), поиск по названию, получение минимального, максимального и среднего значения')
    parser.add_argument('--where', type=str, help='"rating>4.7" Use filters  (> < =)')
    parser.add_argument('--aggregate', type=str, help='"rating=avg" use (avg min max) parametrs')
    parser.add_argument('--file', type=str, help='file path to the file', default="products.csv")
    args = parser.parse_args()

    try:
        products = []
        with open(args.file, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                products.append(row)

        filter = args.where
        aggregate = args.aggregate

        if filter:
            column, value, filter_symb = get_filter_values(filter)
            if column and value:
                filtered_products = get_filtered_products(products, column, value, filter_symb)

                if aggregate:
                    column,value =  get_aggregate_values(aggregate)

                    if column and value:
                        aggregation = get_aggregation_result(filtered_products, column, value)
                        print(tabulate([aggregation], headers = [column], tablefmt="grid"))
                    else:
                        print('Такой агрегации нет')
                else:
                    print(tabulate(filtered_products, headers='keys', tablefmt="grid"))
            else:
                print('Такого фильтра нет')
        else:
            if aggregate:
                column,value =  get_aggregate_values(aggregate)

                if column and value:
                    aggregation = get_aggregation_result(products, column, value)
                    print(tabulate([aggregation], headers = [column], tablefmt="grid"))
                else:
                    print('Такой агрегации нет')
            else:
                print(tabulate(products, headers = 'keys', tablefmt="grid"))

    except FileNotFoundError:
            print('Файл не найден')


if __name__ == '__main__':
    main()