from functions import read_from_csv


from functions import write_list_to_csv

# name_str


def remove_pupil():
    id_pupil = '' 
    

    path_file = 'pupil.csv'
    path_file_rating = 'rating.csv'
    

    pupil_list = read_from_csv(path_file)
   
    rating_list = read_from_csv(path_file_rating) 
    
  
    name_str = input('введите Фамилию и Имя ученика через пробел: > ')
    name= name_str.split()
    id_pupil2 = id_pupil 
    for row in pupil_list: 
                       
        if row[1].lower() == name[0].lower() and row[2].lower() == name[1].lower():
            id_pupil = row[0]
            pupil_list.remove(row)
    for row in rating_list:
        if row[0].lower() == id_pupil2:
            rating_list.remove(row)


    # 


   
    
    pupil_list = write_list_to_csv(path_file)
    print("действие обратное add_pupil()")
    print("при удалении ученика надо также удалить из списка rating.csv все предметы по его ID ")








# if __name__ == '__main__':
#     remove_pupil()
