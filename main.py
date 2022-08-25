NAME_MAIN_FILE = 'file.txt' # name main parse file
NAME_ENGLISH_FILE = 'english.txt' 
NAME_RUSSIAN_FILE = 'russian.txt'


def parse(main_file, engl_file=NAME_ENGLISH_FILE, rus_file=NAME_RUSSIAN_FILE):
    """Parsing function that create two sorted files: russian.txt and english.txt"""
    
    with open(main_file) as file_data:
        all_data = file_data.readlines()
        
        for i in all_data:
            row = i.replace('\n', '').split('\t')
            
            try:
                engl, rus = row[0].split(';'), row[1].split(';')
            except IndexError: continue
            
            engl = [i.strip() for i in engl]
            rus = [i.strip() for i in rus]
            
            for i in set(engl):
                for j in set(rus):
                    with open(engl_file, 'a') as e_file:
                        e_file.write(i + '\n')
                    with open(rus_file, 'a') as r_file:
                        r_file.write(j + '\n')


if __name__ == '__main__':
    try:
        parse(NAME_MAIN_FILE)
    except FileNotFoundError:
        print('No such file!')