# 각 자료실을 다른 클래스로 정의해서 모델을 만드니까 유지관리에 일관성이 없어지는 것 같아요
# global한 변수를 저장할 수 있게 static에 list나 dictionary 형태로 되어있는 환경 변수를 저장하는 파일을 만드려고
# pickle 모듈을 이용해서 만들어두려고 하는데 이 코드를 실행하면 static 내에 환경 변수를 저장하는 pickle 파일들울 만드는게 나을 것 같아요.
# 이러면 사용할 때는 docs/raw_data/해당하는 pickle 파일을 open해서 pickle.load만 해서 쓰면 될 것 같아요

import os
import pickle
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelf_map.settings')
django.setup()


def main():
    f = open("docs/raw_data/archive.pickle", "wb")
    room_nums = {'docs/raw_data/archive1.xlsx': 1, 'docs/raw_data/archive2.xlsx': 2, 'docs/raw_data/archive3.xlsx': 3,
                 'docs/raw_data/archive4.xlsx': 4, 'docs/raw_data/archive5.xlsx': 5, 'docs/raw_data/archive6.xlsx': 6,
                 'docs/raw_data/archive7.xlsx': 7, 'docs/raw_data/archive1_single.xlsx': '1-1', 'docs/raw_data/17자료실_단행본.xlsx': '7-1'}

    pickle.dump(room_nums, f)
    f.close()


if __name__ == '__main__':
    main()
