from functions import read_from_csv


from functions import write_list_to_csv
import csv




def id_pupil():
    id_pupil  = ''
    '''Находит id по имени и фамилии'''
    
     
    

    path_file = 'pupil.csv'
   
    

    pupil_list = read_from_csv(path_file, coding='UTF-8', delim = '|')
   
    
  
    name_str = input('Введите Фамилию и Имя ученика через пробел: > ')
   
    name= name_str.split()
       
        
    
    for row in pupil_list: 
                       
        if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower():
                
            id_pupil = row[0].lower()
            return (id_pupil)

def remove_pupil():
    ''' находим нужное имя (и дополнительно проверям того ли
     ученика планирует удалить пользователь. Далее удаляем ученика из списка
     учеников, и ученика по id из rating'''

    id_pupil_del = id_pupil() #записываем нужный id в переменную

    path_file = 'pupil.csv'
    path_file_rating = 'rating.csv'
    

    pupil_list = read_from_csv(path_file, coding='UTF-8', delim = '|')
    rating_list = read_from_csv(path_file_rating, coding='UTF-8', delim = '|') 

    name_str = input('Еще раз введите Фамилию и Имя ученика через пробел: > ')
    verify_delete  = input(f"Уважаемый, ты уверен, что хочешь удалить ученика из журнала?"
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        name= name_str.split()
       
        
    
    for row in pupil_list: 
                       
        if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower():
            pupil_list.remove(row)
            ''' удаляем имя из списка учеников'''

        for row in rating_list:
            if row[0].lower() == id_pupil_del:
                rating_list.remove(row)
                ''' удаляем id из списка учеников'''

         
                
    
            
        with open(path_file, 'w', encoding='UTF-8') as p_list:
            file_writer = csv.writer(p_list, delimiter = "|" , lineterminator="\n")
            for row in pupil_list:       
                 file_writer.writerow(row) 

        with open(path_file_rating, 'w', encoding='UTF-8') as r_list:
            file_writer = csv.writer(r_list, delimiter = "|" , lineterminator="\n")
            for row in rating_list:       
                file_writer.writerow(row) 
    
           
        print('Ученик успешно удален')        
    else:
        pass
    
  
        
    
       

   




if __name__ == '__main__':
    remove_pupil()