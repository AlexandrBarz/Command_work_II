from constants import ABILITIES as ab
from functions import give_int_num

choose_action = 'выберите пункт меню: '

def get_menu_item():
        for i in enumerate(ab):
            print(*i)
        num = give_int_num(choose_action, min_num = 0, max_num = len(ab))
        return num
