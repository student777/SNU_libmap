import urllib.request
from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf_1, Shelf_2, Shelf_3, Shelf_4, Shelf_5, Shelf_6, Shelf_7
from django.http import Http404

def search_shelf(major_id):
    if 0 < major_id < 100:
        return Shelf_1
    elif 100 < major_id <= 303.4:   # todo
        return Shelf_2
    elif 303.4 < major_id < 400:
        return Shelf_3
    elif 400 <= major_id < 616.855000:
        return Shelf_4
    elif 616.858000 <= major_id < 700:
        return Shelf_5
    elif 700 <= major_id < 900:
        return Shelf_6
    elif 900 <= major_id < 1000: 
        raise Http404('7열람실 자료는 준비중입니다')
    else:
        raise Http404('0~999 범위의 숫자를 입력해 주세요.')


def search_title(text):
    url = 'http://snu-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?ct=facet&fctN=facet_library&fctV=MAIN&rfnGrp=1&rfnGrpCounter=1&vid=82SNU&mode=Basic&ct=Next%20Page&tab=book&fn=search&indx=61&dscnt=0&vl(freeText0)='
    r = urllib.request.urlopen(url+text)
    data = r.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    i = 0
    name_msg_list = []
    for item in soup.find_all(class_="EXLSummaryFields"):
        if i > 15:
            break
        name = item.a.text
        try:
            s = item.find(class_="EXLAvailabilityCallNumber").text
        except AttributeError:
            continue
        ss = re.search(r"[-+]?\d*\.\d+|\d+", s)
        if ss is None:
            sss = s.replace(' ', '')
            location = sss + '은(는) 올바른 입력 값이 아닙니다(TODO)\n'
        else:
            major_id = ss.group()
            Shelf = search_shelf(float(major_id))
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                location = major_id + '/' + shelf.col + shelf.row
            else:
                location = major_id + ' 근처의 도서번호가 존재하지 않습니다(7열람실)\n'
        name_msg_list.append((name, location))
        i += 1
    return name_msg_list
