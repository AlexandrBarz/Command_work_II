from functions import read_from_csv

def get_pupil_list() -> str:
    """
    Считывает csv файл и возвращает строку c именами и фамилиями учащихся (без ID) разделенными "\\n"

    Returns:
    str - список в виде строки
    """ 

    path_file = 'pupil.csv'
    pupil_list = read_from_csv(path_file, coding = 'utf-8', delim = '|')
    string =''
    for row in pupil_list:
        string += row[1]+' '+row[2] +'\n'    
    return string


if __name__ == '__main__':
     get_pupil_list()    