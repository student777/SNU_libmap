from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf
import requests


def search_title(text):
    url = 'http://snu-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?ct=facet&fctN=facet_library&fctV=MAIN&rfnGrp=1&rfnGrpCounter=1&vid=82SNU&mode=Basic&ct=Next%20Page&tab=book&fn=search&indx=61&dscnt=0&vl(freeText0)='
    data = requests.get(url+text)
    soup = BeautifulSoup(data.text, 'html.parser')
    i = 0
    info_list = []
    for item in soup.find_all(class_="EXLSummaryFields"):
        if i > 29:
            break
        name = item.a.text
        try:
            s = item.find(class_="EXLAvailabilityCallNumber").text
        except AttributeError:
            continue
        ss = re.search(r"[-+]?\d*\.\d+|\d+", s)
        if ss is None:
            sss = s.replace(' ', '')
            major_id = '검색 불가'
            location = sss + '검색 불가\n'
        else:
            major_id = ss.group()
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                location = shelf.room_num + '자료실' + shelf.col + shelf.row
            else:
                location = major_id + '\n'
        info_list.append((name, major_id, location))
        i += 1
    return info_list
