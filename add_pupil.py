#Добавление ученика в список учеников
from functions import  add_list_to_csv, string_to_list, read_from_csv
import uuid
# import os.path

def input_firstname()->str:
    """_Ввод фамилии, если пользователь ввел фамилию
    с маленькой буквы- исправит на большую_

    Returns:
        _str_: _фамилия_
    """
    first = input( "Введите фамилию: ") 
    
    if len(first) > 15:
        input_firstname()
    else: return first.title()

def input_lastname()->str: 
    last = input( "Введите имя: ")
    if len(last) > 15:
        input_lastname()
    else: return last.title()

# def generate_new_pupil_id()->int:
#     """Генерируется идентификатор (первичный ключ) для сущности Ученики

#     Returns:
#         str: _возвращается идентификатор ученика_
#     """
#     new_id = 10001
#     filename = 'counter_pupil.txt'
#     if os.path.exists(filename): # если файл существует, открываем на чтение
#         f = open(filename, 'r')
#         line = f.readline() # читаем строку
#         if line != '': # если не пустая строка
#             new_id = int(line) + 1 # итерируем
#         f.close    
    
#     f = open(filename, 'w') # открываем файл на запись
#     f.write(str(new_id)) #запись идентификатора
#     f.close    
        
#     return new_id
  

def add_pupil()->str:
    """_Добавление ученика в файл pupil.csv
    Возвращает id_pupil для дальнейшего использования в rating.csv

    Returns:
     id_pupil   _str_: _идентификатор ученика_
    """

    firstname = input_firstname() 
    lastname = input_lastname()
    id_pupil = uuid.uuid4()
    # id_pupil = generate_new_pupil_id()
    id_pupil= str(id_pupil)
    pupil = id_pupil + " " + firstname + " " + lastname 
    print( "Ученик:\n " + pupil + "\n сохранен!") 
    add_list_to_csv('./Command_work_II/pupil.csv', 'UTF-8', string_to_list(pupil)) #запись в файл
    combined_ids = combine_pupil_and_subject(id_pupil, subject_ids)
    add_list_to_csv("./Command_work_II/rating.csv", "UTF-8",combined_ids ) #запись в файл 
    # return id_pupil


def get_subject_ids(subjects)->list:
    """Формирует список идентификаторов предметов

    Args:
        subjects (_type_): _description_

    Returns:
        list: _список идентификаторов предметов_
    """
    ids = []
    for i in range(1, len(subjects)):
        ids.append(subjects[i][0])
    return ids        

def combine_pupil_and_subject(pupil_id, subject_ids):
    """Формирует для каждого ученика список предметов (по идентификаторам)

    Args:
        pupil_id (_str_): _идентификатор ученика_
        subject_ids (_str_): _идентификатор предмета_

    Returns:
        _list_: _Список идентификатор_ученика, идентификатор_предмета_
    """
    combined = []
    for subject_id in subject_ids:
        el = []
        el.append(pupil_id)
        el.append(subject_id)
        el.append('')
        combined.append(el)
    return combined



subject_list = read_from_csv('./Command_work_II/subjects.csv', 'UTF-8', '|') # чтение файла subjects.csv
subject_ids = get_subject_ids(subject_list)

    
if __name__ == '__main__':
    add_pupil()
 