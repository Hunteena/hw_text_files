import os


class TextFile:
    def __init__(self, file_name, path):
        self.file_name = file_name
        file_path = f'{path}/{file_name}'
        with open(file_path, encoding='utf-8') as file:
            self.lines = file.readlines()
            self.lines_count = len(self.lines)

    def __lt__(self, other):
        return self.lines_count < other.lines_count


def join_files_increasing_line_count(files_list, joined_file_name, folder=None):
    '''
    Записывает данные из списка файлов, находящихся в папке folder, в один файл,
    упорядочив их по количеству строк и добавив информацию о каждом файле,
    и помещает конечный файл в текущую рабочую директорию.
    Если папка не указана, исходные файлы должны быть в текущей рабочей директории.
    '''
    if folder:
        path = f'{os.getcwd()}/{folder}'
    else:
        path = os.getcwd()
        
    text_files_list = []
    for file_name in files_list:
        text_file = TextFile(file_name, path)
        text_files_list.append(text_file)
    text_files_list.sort()
        
    joined_file_path = f'{os.getcwd()}/{joined_file_name}'
    with open(joined_file_path, 'w') as file:
        for text_file in text_files_list:
            file.write(f'{text_file.file_name}\n')
            file.write(f'{text_file.lines_count}\n')
            file.writelines(text_file.lines)
            file.write('\n')
    print(f'Файл {joined_file_name} записан')
        
def main():
    files_list = ['1.txt', '2.txt', '3.txt']
    join_files_increasing_line_count(files_list, 'new_file.txt', 'texts')
    
    
main()
