import openpyxl as openpyxl
import psycopg2

connect = psycopg2.connect(
    host='26.42.46.181',
    port='5432',
    user='postgres',
    password='123123',
    database='Hakaton')


with connect:
    with connect.cursor() as cursor:
        cursor.execute('select * from "public"."Requests"')
        select = cursor.fetchall()
        req_arr = []
        for i in select:
            req_arr.append(list(map(str,f'{i[0]}|{i[1]}|{i[2]}|{i[3]}|{i[4]}|{i[5]}|{i[6]}|{i[7]}|{i[8]}|'.split('|'))))

connect.close()


no_ice_ice1_ice2 = 3
arc4_arc6 = 6
arc7_arc9 = 9



for i in range(47):
    if req_arr[ii][3] == "No ice class" or req_arr[ii][3] == "Ice1" or req_arr[ii][3] == "Ice2" or req_arr[ii][3] == "Ice3":
        req_arr[ii][9] = 3
    elif req_arr[ii][3] == "Arc4" or req_arr[ii][3] == "Arc5" or req_arr[ii][3] == "Arc6":
        req_arr[ii][9] = 6
    elif req_arr[ii][3] == "Arc7" or req_arr[ii][3] or req_arr[ii][3] == "Arc9":
        req_arr[ii][9] = 9
    else:
        print("данные о типе судна неправильные")
        print("пример : no ice class, ice[i] , arc[i]")
        break


"""проверка максимального сплочения льда по всем отрезкам в один день"""

workbook = openpyxl.load_workbook('tab.xlsx')
sheet = workbook.active


MAX_SPLOCHENIYE = []
for i in range(31):
    MAX_SPLOCHENIYE.append(0)


for i in range(1, 31):
    for row in sheet.iter_rows(min_row=1, max_row=14, min_col=i, max_col=i, values_only=True):
        cell_value_a, = row
        cell_value_a = int(cell_value_a)
        if cell_value_a > MAX_SPLOCHENIYE[i-1]:
            MAX_SPLOCHENIYE[i-1] = cell_value_a

for i in range(31):
    print(f"в день {i+1} ")

    for ii in range(47):
        print(f"корабль номер {ii+1} : ", end = "")

        if req_arr[i][9] == 3:
            if MAX_SPLOCHENIYE[i] <= 3:
               print("пройдет самостоятельно")
            elif MAX_SPLOCHENIYE[i] <= 6:
                print("проплывет с сопровождением")
            elif MAX_SPLOCHENIYE[i] > 6:
                 print("плыть запрещеено")
        elif req_arr[i][9] == 6:
            if MAX_SPLOCHENIYE[i] <=6:
                print("пройдет самостоятельно")
            else:
                print("проплывет с сопровождением")
        if req_arr[i][9] == 9:
            print("пройдет самостоятельно")
