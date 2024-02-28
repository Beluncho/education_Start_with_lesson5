import os


def view_file():
    """

    :return: файлы
    """
    with os.scandir(path='.') as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                print(entry.name)
    return entry.name


def view_dir():
    """

    :return: директории
    """
    with os.scandir(path='.') as it:
        for entry1 in it:
            if not entry1.name.startswith('.') and entry1.is_dir():
                print(entry1.name)
    return entry1.name


def save_file():
    
    with os.scandir(path='.') as it:

        entry_list = []
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():

                entry_list.append(entry.name)   # добавляем в список только файлы

        entry_dict = dict.fromkeys(['files'], entry_list)

    return entry_dict


def save_dir():
    """

    :return: словарь директории:значения
    """
    with os.scandir(path='.') as it:
        entry_list = []
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                entry_list.append(entry.name)  # добавляем в список только директории
        entry_dict = dict.fromkeys(['dirs'], entry_list)

    return entry_dict





