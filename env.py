# 각 자료실을 다른 클래스로 정의해서 모델을 만드니까 유지관리에 일관성이 없어지는 것 같아요
# global한 변수를 저장할 수 있게 static에 list나 dictionary 형태로 되어있는 환경 변수를 저장하는 파일을 만드려고
# pickle 모듈을 이용해서 만들어두려고 하는데 이 코드를 실행하면 static 내에 환경 변수를 저장하는 pickle 파일들울 만드는게 나을 것 같아요.
# 이러면 사용할 때는 static/해당하는 pickle 파일을 open해서 pickle.load만 해서 쓰면 될 것 같아요

import os
import pickle
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelf_map.settings')
import django
django.setup()


def main():
    f = open("static/자료실.pickle", "wb")
    room_nums = {'static/1자료실.xlsx': 1, 'static/2자료실.xlsx': 2, 'static/3자료실.xlsx': 3, 'static/4자료실.xlsx': 4,
                 'static/5자료실.xlsx': 5, 'static/6자료실.xlsx': 6, 'static/7자료실.xlsx': 7}
    pickle.dump(room_nums, f)
    f.close()

if __name__ == '__main__':
    main()
