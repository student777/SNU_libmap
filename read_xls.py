import xlrd
import pickle
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelf_map.settings')
import django
django.setup()
import shelf_map.models
from django.core.exceptions import ValidationError


def main():
    f = open("static/자료실.pickle", "rb")
    room_nums = pickle.load(f)
    f.close()

    for room_name in room_nums.keys():
        filename = room_name
        workbook = xlrd.open_workbook(filename)
        workbook_index = workbook.sheet_by_index(0)

        for i in range(0, int(workbook_index.nrows/2)):
            major_id_list = workbook_index.row_values(2*i)
            minor_id_list = workbook_index.row_values(2*i+1)

            for j in range(0, len(major_id_list)):
                try:
                    shelf_map.models.create_shelf(room_nums[room_name], chr(j+65), str(i/2+1), major_id_list[j], minor_id_list[j])
                except ValidationError:
                    continue

        print(room_name+'자료실 추가 완료')
if __name__ == '__main__':
    main()
