from pathlib import Path

def get_cats_info(path):
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            list = []
            if not lines:
                print('File is empty')

        for line in lines:
            strings = line.split(',')
            dictionary = {"id": strings[0], "name": strings[1], "age": strings[2]}
            list.append(dictionary)
        return list
            
    except FileNotFoundError:
        print('No such file or directory')
    except IndexError:
        print('List index out of range')
    
if __name__ == '__main__':
    cats_info = get_cats_info('Cats.txt')
    print(cats_info)


       

