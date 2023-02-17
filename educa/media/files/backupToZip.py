#! python3
# backupToZip.py - копирует папку вместе с её содержимым в zip-файл с инкрементируемым номером копии в имени файла.

import os
import zipfile


def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Создаётся файл %s...' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавление файлов из папки %s...' % foldername)
        # добваить в ZIP-файл текущую папку.
        backupZip.write(foldername)
        # добваить в ZIP-файл все файлы из данной папки.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # не создавать резервные копии ZIP-файлов
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Ready')


backupToZip('D:\pythonProjects\scrab_bundestag')
