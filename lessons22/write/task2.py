import os

def write_file(file_path, name_file):
    current_file = open(file_path, 'r', encoding='utf-8')
    scripText = current_file.read()
    current_file.close()

    script_file = open('ScriptFile.txt', 'a', encoding='utf-8')
    script_file.write(f'*************** {name_file} *************** \n\n')
    script_file.write(scripText+'\n\n')
    script_file.close()


def recurs_file(path):
    for i in os.listdir(path):
        if i[0] != '.':
            new_sercher = os.path.join(path, i)
            if os.path.isdir(new_sercher):
                recurs_file(new_sercher)
            else:
                write_file(new_sercher, i)


serch_file = os.path.join('..', '..')

recurs_file(serch_file)