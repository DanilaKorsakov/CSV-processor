# Обработка CSV файла

Данная программа обрабатывает CSV файл двумя способами с помощью:
1. фильтрации с операторами «больше», «меньше» и «равно»
1. агрегации с расчетом среднего (avg), минимального (min) и максимального (max) значения

## Как установить

Для запуска программы необходимо установить Python от 3 версии.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:  

```
pip install -r requirements.txt
``` 

## Как работать с проектом

Запустить проект можно без каких-либо аргументов, в итоге просто получится красивый вывод с данными из csv файла

```
python main.py
```

![Запуск без аругментов](https://github.com/DanilaKorsakov/CSV-processor/blob/main/images/1.PNG)

Запустить проект можно указав любой путь до вашего CSV файла, делаетеся это через аргуменn `file`

```
python main.py --file products.csv
```

Для фильтрации продуктов есть аргмуент `where`, который работает со всеми значениями(строки и числа)

```
python main.py --file products.csv  --where "rating>4.7"
```
Результат работы:

![Рейтинг>4.7](https://github.com/DanilaKorsakov/CSV-processor/blob/main/images/2.PNG)

```
python main.py --file products.csv  --where "brand=apple"
```
Результат работы:

![Рейтинг>4.7](https://github.com/DanilaKorsakov/CSV-processor/blob/main/images/5.PNG)

Для агрегации есть агрумент `aggregate`, который работает только с числовыми значениями

```
python main.py --file products.csv --aggregate "rating=max"
```
Результат работы:

![Рейтинг>4.7](https://github.com/DanilaKorsakov/CSV-processor/blob/main/images/3.PNG)

Эти два аргумента можно использовать одновременно, например получая максимальное значение рейтинга определенного бренда

```
python main.py --file products.csv --aggregate "rating=max"
```
Результат работы:

![Рейтинг>4.7](https://github.com/DanilaKorsakov/CSV-processor/blob/main/images/4.PNG)