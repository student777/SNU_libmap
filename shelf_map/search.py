from bs4 import BeautifulSoup
import re
from shelf_map.models import Shelf
import requests
from django.http import Http404


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
            # TODO: minor_id 정규표현식
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
            #TODO: shelf=find_shelf(major_id, minor_id); name, room_num, colrow = shelf.name, shelf.major_id, shelf.minor, shelf.row+shelf.col;
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).exclude(room_num='1-1').exclude(room_num='7-1').order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                room_num = shelf.room_num
                colrow = shelf.col + shelf.row
            else:
                location = major_id + '\n'
        info_list.append((name, major_id, room_num, colrow))
        i += 1
    return info_list


def find_shelf(major_id, minor_id=''):
    if Shelf.objects.filter(major_id=major_id, major_leadingChr=None).exclude(room_num='1-1').exclude(room_num='7-1').count() > 1:
        if minor_id is '':
            result = Shelf.objects.filter(major_id=major_id, major_leadingChr=None).exclude(room_num='1-1').exclude(room_num='7-1').first()
        else:
            result = Shelf.objects.filter(major_id=major_id, minor_id__lte=minor_id, major_leadingChr=None).exclude(room_num='7-1').exclude(room_num='1-1').order_by('minor_id').last()
    else:
        result = Shelf.objects.filter(major_id__lte=major_id, major_leadingChr=None).exclude(room_num='7-1').exclude(room_num='1-1').order_by('major_id').last()
    if result is None: 
        result = Shelf(room_num='검색불가', col='', row='', major_id=0, minor='')
    return result
