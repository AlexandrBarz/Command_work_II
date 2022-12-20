import time

from functions import read_from_csv, write_list_to_csv

path_pupil = 'pupil.csv'
path_subj = 'subjects.csv'
path_reit = 'rating.csv'
coding = 'UTF-8'

def edit_pupil():
    find = []
    data = read_from_csv(path_pupil, coding, '|')
    print('Если запрос по одному критерию, поставьте проблел в пустом поле')
    search_last = input('Введите Фамилию ученика\n>')
    search_name = input('Введите Имя ученика\n>')
    for item in data:
        if search_last.capitalize() in item[1] or search_name.capitalize() in item[2]:
            find.append(item)
            data.remove(item)
    if len(find) == 1:
        print('Ученик найден')
        print(*find)
        find[0][1] = input('Введите фамилию ученика:\n>')
        find[0][2] = input('Введите имя ученика:\n>')
        print(find)
        data.append(find[0])
        print(data)
        write_list_to_csv(path_pupil, coding, data)
        print('Редактирование прошло успешно')

def edit_asses():
    find = []
    data_1 = read_from_csv(path_pupil, coding, '|')
    print('Если запрос по одному критерию, поставьте проблел в пустом поле')
    search_last = input('Введите Фамилию ученика\n>')
    search_name = input('Введите Имя ученика\n>')

    for item in data_1:
        if search_last.capitalize() in item[1] or search_name.capitalize() in item[2]:
            find.append(item)
            data_1.remove(item)
    if len(find) == 1:
        print('Ученик найден')
        print(*find)
        id_pupil = find[0][0]
        search_pupil = find[0][1] + " " + find[0][1]
    else:
        print("По вашему запросу учеников не найдено или найденных более одного\n")
        print("Уточните свой запрос")
        time.sleep(1)
        return
    find = []
    search_subj = input('Введите название предмета\n>')
    data_2 = read_from_csv(path_subj, coding, '|')
    for item in data_2:
        if search_subj.capitalize() in item[1]:
            find.append(item)
    if len(find) == 1:
        print('И предмет такой есть\n')
        id_subj = find[0][0]
        subj_name = find[0][1]
        find = []
    else:
        print('Предмет не найден\nУточните свой запрос')
        time.sleep(1)
        change_pupil()
    find = []
    data_reit = read_from_csv(path_reit, coding, '|')
    for item in data_reit:
        if id_pupil == item[0] and id_subj == item[1]:
            find.append(item)
            data_reit.remove(item)
            break
    print(len(find))
    if len(find) > 0:
        last_asses = find[0][2]
        print(f'Актуальные оценки ученика "{search_pupil}" по предмету "{subj_name}": {last_asses}')
        find[0][2] = input('Внесите корректировки в оценки ученика через запятую и пробел:\n>')
        data_reit.append(find[0])
        write_list_to_csv(path_reit, coding, data_reit)
        print('Корректировки успешно внесены')
        exit()
    else:
        print('У выбранного ученика нет таких предметов\n'
              'Попробуйте ввести поисковый запрос еще раз')
        change_pupil()

def change_pupil():

    resp = input('1. Отредактировать профиль ученика\n'
                  '2. Отредактировать оценки ученика по предмету\n>')
    try:
        resp = int(resp)
    except:
        print("Ошибка.Введите цифры")
        return
    if resp == 1:
        edit_pupil()
    elif resp == 2:
        edit_asses()
    else:
        return


if __name__ == '__main__':
    change_pupil()