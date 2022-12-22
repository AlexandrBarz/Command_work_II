import sys
from functions import read_from_csv, write_list_to_csv, give_int_num
from get_pupil_list import get_pupil_list

def get_subject_list() -> str:
    """
    Считывает csv файл и возвращает строку c предметами (без ID)

    Returns:
    str - список в виде строки
    """ 

    path_file = 'subjects.csv'
    subjects_list = read_from_csv(path_file, coding = 'utf-8', delim = '|')
    string =''
    for row in subjects_list:
        string += row[1] +'\n'    
    return string


def add_rating():
    """
    Функция запрашивает у пользователя фамилию ученика, предмет, оценку по предмету и заносит в ведомость.

    Return:
    вносит оценки в ведомость (файл)
    """
    coding = 'utf-8'
    delim = '|'
    id_pupil = ''
    id_subject = ''
    path_file = 'pupil.csv'
    path_file_rating = 'rating.csv'
    path_file_subject = 'subjects.csv'

         
    pupil = input('Введите фамилию ученика для выставления оценки --> ')
    pupil_list = read_from_csv(path_file, coding, delim)
    for row in pupil_list:
        if row[1].lower() == pupil.lower():
            id_pupil = row[0]
    if len(id_pupil) < 1:
        print(f'\nУченик {pupil.title()} не найден в списке. Проверьте корректность ввода фамилии.')
        string = get_pupil_list()
        sys.exit(f'\n {string}')   
            
    subject = input('Введите предмет для выставления оценки --> ')
    subjects_list = read_from_csv(path_file_subject, coding, delim)
    for row in subjects_list:
        if row[1].lower() == subject.lower():
            id_subject = row[0]
    if len(id_subject) < 1:
        print(f'\nПредмет {subject} не найден. Проверьте название предмета.')
        string = get_subject_list()
        sys.exit(f'\n {string}')
                       
    rating = str(give_int_num('Введите оценку, которую хотите поставить --> ', 1, 5))
    raiting_list = read_from_csv(path_file_rating, coding, delim)
    for row in raiting_list:
        if id_pupil == row[0] and id_subject == row[1]:
            rating_list = (row[2].split(', '))
            rating_list.append(rating)
            row[2] = ', '.join(rating_list).lstrip(', ')
    write_list_to_csv(path_file_rating, coding, raiting_list)
    print(f'Учащемуся {pupil.title()} была проставлена оценка {rating} по предмету {subject.lower()}')

  
if __name__ == '__main__':
    add_rating()