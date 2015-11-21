import urllib.request
from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf


def search(text):
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
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                location = major_id + '/' + shelf.col + shelf.row
            else:
                location = major_id + ' 근처의 도서번호가 존재하지 않습니다\n'
        name_msg_list.append((name, location))
        i += 1
    return name_msg_list
