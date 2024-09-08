from os import listdir
from Config import *


def _get_not_idea(path):
    direct: list = listdir(path)
    if '.idea' in direct:
        direct.remove('.idea') # удаляем.idea
    return direct

def _get_paths(path, name_directory):
    return path + '\\' + name_directory


def chec_structure(path):
    if _get_not_idea(path) == ABSOLUTE_DIRECT:
        pass
    else:
        print("\033[31m {}".format(f'\nНе правильная структура проекта!!!\nДолжно быть вот так -> {temp_proect}'))
        return False
    return True # если все хорошо, то возвращаем True

def check_structure_shild(path):
    try:
        if listdir(_get_paths(path, 'data')) == CHILD_DIRECT['data']:
            return True
        if listdir(_get_paths(path, 'layout')) == CHILD_DIRECT['layout']:
            return True
        else:
            print("\033[31m".format(f'\nНеправильная структура папки data или layout\nДолжно быть вот так:\nпапка data = {temp_data}\nпапка layout = {temp_layout}'))
            return False
    except FileNotFoundError:
        print("\033[31m".format(f'Отсутсвуют папки data или layout'))
        return False

