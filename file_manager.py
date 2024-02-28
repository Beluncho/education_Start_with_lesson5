import json
import os
import shutil
import sys

import use_function
import victory
from def_for_manager import view_file, view_dir, save_dir, save_file

while True:
    print('1. Add new folder')
    print('2. Del file/folder')
    print('3. Copy file/folder')
    print('4. View directory')
    print('5. View folder')
    print('6. View file')
    print('7. View sys')
    print('8. Creator')
    print('9. Play quiz')
    print('10. Balance')
    print('11. Change directory')
    print('12. Exit')

    choice = input('Choice item: ')
    if choice == '1':
        new_folder = input('Name new folder: ')
        for i in range(1):
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
        pass

    elif choice == '2':
        del_folder = input('Name of del folder/file: ')
        os.rmdir(del_folder)
        pass

    elif choice == '3':
        copy_folder = input(' What folder/file your copy?: ')
        new_folder_copy = input('Name your copy')
        shutil.copy(copy_folder, new_folder_copy)
        pass

    elif choice == '4':
        print(sys.path)
        pass

    elif choice == '5':

        view_dir()
        pass

    elif choice == '6':
        while True:
            print('1.View file')
            print('2. Save contents of the working directory in listdir.txt')
            print('3. Return in file manager')
            choice_in = input('Choice item: ')
            if choice_in == '1':
                view_file()
            elif choice_in == '2':
                save_listdir = {**save_file(),
                                **save_dir()}

                with open('listdir.txt', 'w') as f:
                    json.dump(save_listdir, f)

            elif choice_in == '3':
                break
            else:
                pass
        pass

    elif choice == '7':
        print(sys.platform)
        pass
    elif choice == '8':
        print('Beluncho')
        pass
    elif choice == '9':
        victory.victory()
        pass
    elif choice == '10':
        use_function.balance_fun()
        pass
    elif choice == '11':
        directory = os.getcwd()
        print(directory)
        os.chdir(input('new directory: '))
        directory = os.getcwd()
        print(directory)
    elif choice == '12':

        break


