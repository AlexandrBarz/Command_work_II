import sys
from functions import read_from_csv, write_list_to_csv
from get_pupil_list import get_pupil_list


def get_pupil_summary():
    # print("спросить ФИ ученика, сформировать список предметов + оценок за них, вывести это в консоль или файл")

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
  
    name_str = input('введите Фамилию и Имя ученика через пробел: > ')
    name= name_str.split()
    for row in pupil_list:                   
        if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower(): 
            id_pupil = row[0]
            fio = row[1] + " " + row[2]
     
    if len(id_pupil) < 1:
        print(f'\nУчащегося {name_str} не найдено. Проверьте Фамилию и Имя ученика.')        
        string = get_pupil_list()
        sys.exit(f'Список класса:\n {string}')            
       
    print(fio)
    print(id_pupil)
   
    find = []   
    for i in range (len(rating_list)):            
        if id_pupil == rating_list[i][0]:
            find.append(rating_list[i][2])    
         
    find.append(0)  
    for i in range (1,len(subject_list)):
        print(subject_list[i][1], find[i-1])
        
          

    # subj = input('введите предмет: > ')
    # for row in subject_list:              
    #     if row[1].lower() == subj.lower():
    #         id_subj = row[0]  

    # if len(id_subj) < 1:
    #     print(f'учебного предмета {subj} не найдено.')        
    #     string =''
    #     for row in subject_list:
    #         string += row[1]+'\n'
    #     sys.exit(f'Список предметов:\n {string}')
    
    
    # rating_list = read_from_csv(path_file_rating, coding, delim)     
    # for row in rating_list:
                        
    #     if row[0] == id_pupil and row[1] == id_subj:
    #         rating_string = row[2] 

    # if rating_string == "":
    #     print(f"\nУчащийся {name[0].title()} {name[1].title()} не имеет оценок по предмету: {subj}.")
    # else:
    #     print(f"\nУчащийся {name[0].title()} {name[1].title()} имеет следующие оценки по предмету\n{subj}:> {rating_string}")

# data = read_from_csv(path_pupil, coding, '\n')
# find = []
# search_last_name = input('Введите Фамилию и (или) Имя ученика\n>')

# for item in pupil_list:
#     if search_last_name.capitalize() in str(item):
#         find.append(item[0])
          
# print(find)

if __name__ == '__main__':
    get_pupil_summary()