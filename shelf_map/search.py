import urllib.request
from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf


def search(text):
    url = 'http://snu-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?ct=facet&fctN=facet_library&fctV=MAIN&rfnGrp=1&rfnGrpCounter=1&vid=82SNU&mode=Basic&ct=Next%20Page&tab=book&fn=search&indx=61&dscnt=0&vl(freeText0)='
    # r = urllib.request.urlopen(url+text)
    r = urllib.request.urlopen(url+text)
    data = r.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    result_msg = text + '에 대한 검색결과(최대 15권 검색)\n'
    i = 0
    for item in soup.find_all(class_="EXLAvailabilityCallNumber"):
        if i > 15:
            break
        msg = ''
        s = str(item.contents[0])
        # ss = re.match("\d+.\d+", s)
        ss = re.search(r"[-+]?\d*\.\d+|\d+", s)
        if ss is None:
            sss = s.replace(' ', '')
            msg = sss + '은(는) 올바른 입력 값이 아닙니다(TODO)\n'
        else:
            major_id = ss.group()
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                msg = major_id + '은(는)' + shelf.col + shelf.row + '에 있습니다\n'
            else:
                msg = major_id + ' 근처의 도서번호가 존재하지 않습니다\n'
        result_msg = result_msg + msg
        i += 1
    return result_msg
