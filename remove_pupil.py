from functions import read_from_csv


from functions import write_list_to_csv
import csv




def remove_pupil():
    id_pupil  = ''
    id_pupil2 =''
     
    

    path_file = 'pupil.csv'
    path_file_rating = 'rating.csv'
    

    pupil_list = read_from_csv(path_file, coding='UTF-8', delim = '|')
   
    rating_list = read_from_csv(path_file_rating, coding='UTF-8', delim = '|') 
    
  
    name_str = input('Введите Фамилию и Имя ученика через пробел: > ')
    verify_delete  = input(f"Уважаемый, ты уверен, что хочешь удалить ученика из журнала?"
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        name= name_str.split()
       
        
    
        for row in pupil_list: 
                       
            if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower():
                id_pupil2 = id_pupil 
                id_pupil = row[0].lower()
                
                pupil_list.remove(row)
        for row in rating_list:
            if row[0].lower() == id_pupil2:
                rating_list.remove(row)
            
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
    
    # row_del = [row for row in rating_list if row[0]==id_pupil2] (можно в таком виде?)
    # rating_list.remove(row_del)
        
    
       

    # Совсем не уверена, что это может работать(((
    #  Может быть надо совсем по другой логике пойти. 

    # print("действие обратное add_pupil()")
    # print("при удалении ученика надо также удалить из списка rating.csv все предметы по его ID ")








# if __name__ == '__main__':
#     remove_pupil()