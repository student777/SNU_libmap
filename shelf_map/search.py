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
        link = 'http://snu-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/' + item.a['href']
        if item.find(class_="EXLAvailabilityCollectionName") is None or item.find(class_="EXLAvailabilityCollectionName").text.find('단행본자료실') is -1:
            continue # 규장각, 수원보존도서관, 1-1 및 7-1자료실(?), KOCKA서가 등 제외
        if item.find(class_="EXLResultStatusNotAvailable") is not None:
            status = False
        else:
            status = True
        try:
            num1 = item.find(class_="EXLAvailabilityCallNumber").text # major_id
        except AttributeError:
            continue
        num2 = re.search(r"[a-zA-Z]?\d*\.\d+|[a-zA-Z]?\d+", num1)
        if num2 is None:
            major_id = '확인불가'
            minor_id = ''
            room_num = '확인불가'
            colrow = ''
        elif num1.find('大') is not -1: # ex)大 294 D65b
            minor_id = num1.split()[2]
            major_id = '大' + num2.group()
            room_num = '검색 미지원'
            colrow = ''
        elif num2.group()[0].isalpha(): # ex)K781
            major_id = num2.group()
            minor_id = num1.split()[1]
            room_num = '검색 미지원'
            colrow = ''
        else: # ex) 821.123
            major_id = num2.group()
            minor_id = num1.split()[1]
            shelf = find_shelf(major_id, minor_id)
            room_num = shelf.room_num + '자료실'
            colrow = shelf.row+shelf.col
        info_list.append((name, major_id, minor_id, room_num, colrow, link, status))
        i += 1
    return info_list


def find_shelf(major_id, minor_id):
    shelf_list = Shelf.objects.exclude(room_num='1-1').exclude(room_num='7-1').filter(major_leadingChr=None)
    if shelf_list.filter(major_id=major_id).count() >= 1:
        result = shelf_list.filter(major_id=major_id).filter(minor_id__lte=minor_id).last()
    elif shelf_list.filter(major_id__lte=major_id):
        result = shelf_list.filter(major_id__lte=major_id).last()
    else:
        result = Shelf(room_num='검색불가', col='', row='', major_id=0, minor='')
    return result
