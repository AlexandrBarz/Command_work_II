import time

from functions import read_from_csv, write_list_to_csv

path_pupil = 'pupil.csv'
path_subj = 'subjects.csv'
path_reit = 'rating.csv'
coding = 'UTF-8'
def change_pupil():
    find = []
    resp = input('1. Отредактировать профиль ученика\n'
                  '2. Отредактировать оценки ученика по предмету\n>')
    try:
        resp = int(resp)
    except:
        print("Ошибка.Введите цифры")
        return
    if resp == 1:
        data = read_from_csv(path_pupil, coding, '\n')
        search_last_name = input('Введите Фамилию и (или) Имя ученика\n>')

        for item in data:
            if search_last_name.capitalize() in str(item):
                find.append(item[0])
                data.remove(item)
        print(len(find))
        if len(find) != 0:
            print('Ученик найден')
            print(*find)
            hash = find[0][:37]
            last = input('Введите фамилию ученика:\n>') + '|'
            name = input('Введите имя ученика:\n>') + '|'
            find[0] = hash+last+name
            data.append(find)
            write_list_to_csv(path_pupil, coding , data)
            print('Редактирование прошло успешно')
        else:
            print("По вашему запросу учеников не найдено или найденных более одного")
            print("Уточните свой запрос")

    elif resp == 2:
        data_1 = read_from_csv(path_pupil, coding, '\n')
        search_pupil = input('Введите Фамилию и (или) Имя ученика\n>')
        for item in data_1:
            if search_pupil.capitalize() in str(item):
                find.append(item[0])
                break
        if len(find)>0:
            print("Ученик найден")
            id_pupil = find[0][:36]
            search_pupil = find[0][37:].replace('|',' ')
            print(f'\n{search_pupil}\n')
        else:
            print("По вашему запросу учеников не найдено или найденных более одного\n")
            print("Уточните свой запрос")
            time.sleep(1)
            return
        find = []
        search_subj = input('Введите название предмета\n>')
        data_2 = read_from_csv(path_subj, coding, '\n')
        for item in data_2:
            if search_subj.capitalize() in str(item):
                find.append(item[0])
        # id_subj = find[0][:5]
        # subj_name = find[0][6:]
        if len(find)>0:
            id_subj = find[0][:5]
            subj_name = find[0][6:]
            find = []
            print('И предмет такой есть\n')
            data_reit = read_from_csv(path_reit, coding, '\n')
            for item in data_reit:
                if id_pupil in str(item) and id_subj in str(item):
                    find.append(item[0])
                    data_reit.remove(item)
                    break
            else:
                print('У выбранного ученика нет таких предметов\n'
                      'Попробуйте ввести поисковый запрос еще раз')
                change_pupil()

            fir_part = find[0][:43]
            last_asses = find[0][43:-1]
            print(f'Актуальные оценки ученика "{search_pupil}" по предмету "{subj_name}": {last_asses}')
            last_asses = input('Внесите корректировки в оценки ученика через запятую и пробел:\n>')+'|'
            res = fir_part + last_asses
            find = []
            find.append(res)
            data_reit.append(find)
            write_list_to_csv(path_reit, coding, data_reit)
            print('Корректировки успешно внесены')
            exit()
        else:
            print('Предмет не найден\nУточните свой запрос')
            time.sleep(1)
            change_pupil()
    else:
        return



if __name__ == '__main__':
    change_pupil()    