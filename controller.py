from user_interface import get_menu_item
import add_pupil, add_pupil_rating
import get_pupil_summary
import get_pupil_list, get_pupil_subject
import remove_pupil, change_pupil_data
import sys

def start():
    while True:
        menu_item = get_menu_item()

        if menu_item == 1:
            add_pupil.add_pupil()
            а = menu_item

        elif menu_item == 2:
            add_pupil_rating.add_rating()
            а = menu_item

        elif menu_item == 3:
            get_pupil_summary.get_pupil_summary()  
            а = menu_item
            
        elif menu_item == 4:
            get_pupil_subject.get_pupil_subject()
            а = menu_item
            
        elif menu_item == 5:
            remove_pupil.remove_pupil() 
            а = menu_item
        
        elif menu_item == 6:
            change_pupil_data.change_pupil()
            а = menu_item

        elif menu_item == 7:
            string = get_pupil_list.get_pupil_list()
            print(f'\nСписок учащихся:\n {string}')             
      
        elif menu_item == 0:
            sys.exit('работа завершена') 
        input('---< для продолжения нажмите Enter >---')   