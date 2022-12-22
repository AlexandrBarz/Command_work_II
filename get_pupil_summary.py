from functions import read_from_csv
from get_pupil_list import get_pupil_list

# Функция запрашивает у пользователя Фамилию и Имя обучающегося и
# выводит успеваемость по всем предметам в консоль")

def get_pupil_summary():
    
    coding = 'utf-8'
    delim = '|'
    rating_string =''
    id_pupil = ''
    id_subj = ''
    
    fio = ""

    path_file = 'pupil.csv'
    path_file_rating = 'rating.csv'
    path_file_subject = 'subjects.csv'

    pupil_list = read_from_csv(path_file, coding, delim)
    subject_list = read_from_csv(path_file_subject, coding, delim) 
    rating_list = read_from_csv(path_file_rating, coding, delim) 
  
    name_str = input('Введите Фамилию и Имя обучающегося через пробел: > ')
    name= name_str.split()
    for row in pupil_list:                   
        if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower(): 
            id_pupil = row[0]
            fio = row[1] + " " + row[2]
     
    if len(id_pupil) < 1:
        print(f'\nОбучающегося {name_str} не найдено. Проверьте Фамилию и Имя обучающегося.')        
        string = get_pupil_list()
        print(f'Список класса:\n {string}')
        return None
       
     
    find = []   
    for i in range (len(rating_list)):            
        if id_pupil == rating_list[i][0]:
            find.append(rating_list[i][2])    
         
    find.append(0)  
    for i in range (1,len(subject_list)):
        print(subject_list[i][1], find[i-1])
        

if __name__ == '__main__':
    get_pupil_summary()