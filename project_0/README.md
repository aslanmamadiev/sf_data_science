# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README/md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README/md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат)    
[6. Выводы](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

### Описание проекта  
Угадать загаданное компьютером число за минимальное число попыток.  

**1** • [2](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем) • [3](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных) • [4](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом) • [5](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат) • [6](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

---

### Какой кейс мы решаем?  
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**  
- Компьютер загадывает целое число **от 1 до 100**, и нам нужно его угадать. Под "угадать" подразумевается "написать программу, которая угадывает число"
- Алгоритм учитывает информацию о том, больше / меньше ли случайное число, чем нужное нам

**Метрика качества**  
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем** \
Учимся писать хороший `код` на **Python**  

[1](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Описание-проекта) • **2** • [3](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных) • [4](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом) • [5](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат) • [6](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

---

### Краткая информация о данных  
[1](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Описание-проекта) • [2](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем) • **3** • [4](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом) • [5](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат) • [6](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

---

### Этапы работы над проектом
1. Вспоминаем математику и метод приближения, при котором число определяется делением ряда пополам при каждой итерации.
2. Для чисел от 1 до 100 это можно обосновать примерно так: $\dfrac{1+100}{2^{n}}\rightarrow 1$ при $n\rightarrow 7$ (математически запись может быть немного неккоректна, но она необходима для отображения доносимого смысла). То есть наша программа способна вычислить нужное число максимум за 7 попыток.
3. Составляем функцию с циклом `while`, в котором загаданное нами число будет принимать граничное значение, каждый раз вдвое уменьшая диапазон (при этом используется целочисленное деление!).
При нахождении искомого числа счётчик сбрасывается благодаря `break`
4. Запускаем код для проверки

[1](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Описание-проекта) • [2](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем) • [3](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных) • **4** • [5](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат) • [6](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

---

### Результат
1. Результат работы приведён в файле game_v3.py
2. Каждый раз при определении загаданного числа, счётчик попыток сбрасывается до 0
3. Среднее количество попыток составляет меньше 7
[1](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Описание-проекта) • [2](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем) • [3](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных) • [4](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом) • **5** • [6](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Выводы)

---

### Выводы
По итогам выполненной работы достигнуты намеченные цели: был реализован один из методов, используемых в информатике, благодаря которому удалось существенно снизить среднее количество итераций для нахождения загаданного числа.
[1](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Описание-проекта) • [2](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем) • [3](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных) • [4](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом) • [5](https://github.com/aslanmamadiev/sf_data_science/tree/main/project_0/README.md#Результат) • **6**
