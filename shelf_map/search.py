from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf
from django.http import Http404
import requests


def search_title(text):
    url = 'http://snu-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?ct=facet&fctN=facet_library&fctV=MAIN&rfnGrp=1&rfnGrpCounter=1&vid=82SNU&mode=Basic&ct=Next%20Page&tab=book&fn=search&indx=61&dscnt=0&vl(freeText0)='
    data = requests.get(url+text)
    soup = BeautifulSoup(data.text, 'html.parser')
    i = 0
    info_list = []
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
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                location = shelf.room_num + '열람실 ' + shelf.col + shelf.row
            else:
                location = major_id + ' 근처의 도서번호가 존재하지 않습니다(7열람실)\n'
        info_list.append((name, major_id, location))
        i += 1
    return info_list
