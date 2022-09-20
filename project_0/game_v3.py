'''
Игра "Угадай число!" (улучшенная версия)

Компьютер сам загадывает и сам отгадывает число, пспользуя минимум попыток

'''

import numpy as np


def random_predict(number: int=None) -> int:  # Тип данных для ввода -> на выходе
    '''
    Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to None.

    Returns:
        int: Число попыток
        
    '''
    
    count = 0
    a = 1
    b = 100
    
    while True:
        predict_number = np.random.randint(a, b)  # Предполагаемое число
        
        if number == predict_number:  # Модифицируем функцию, используя метод деления пополам
            break
        else:
            while number != predict_number:
                number = (a+b) // 2
                count += 1
                if number < predict_number:
                    a = number
                elif number > predict_number:
                    b = number
            break
    return count


print(f'Количество попыток: {random_predict()}')


def score_game(random_predict):
    '''
    За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания
        
    Returns:
        int: Среднее количество попыток
    
    '''
    
    count_ls = []  # Список сохранения количества попыток
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000))  # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))  # Находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


if __name__ == '__main__':
    score_game(random_predict)