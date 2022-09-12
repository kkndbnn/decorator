from datetime import datetime
import os

def param_decor(path):
    def decor(old_function):
        def new_function(*args, **kwargs):
            if not os.path.isdir('logs'):
                os.mkdir('logs')
            with open("logs/info.txt", 'a', encoding='UTF-8') as f:
                f.write(f'Функция "{old_function.__name__}" была вызвана.' + '\n')
                f.write(f'Дата и время вызова: {datetime.now()}' + '\n')
                f.write(f'Аргументы: {args}' + '\n')
                result = old_function(*args, **kwargs)
                f.write(f'Возвращаемое значение: {result}' + '\n')
                f.write(f'Путь к файлу: {path}' + '\n')
            return result

        return new_function

    return decor