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
        try:
            num1 = item.find(class_="EXLAvailabilityCallNumber").text
        except AttributeError:
            continue
        if item.find(class_="EXLAvailabilityCollectionName").text.find('단행본') is -1:
            continue
        # if item.find(class_="EXLResultStatusNotAvailable") is not None:
        num2 = re.search(r"[-+]?\d*\.\d+|\d+", num1)
        if num2 is None:
            major_id = '확인불가'
            minor_id = ''
            room_num = '확인불가'
            colrow = ''
        else:
            major_id = num2.group()
            try:
                minor_id = num1.split()[1]
                if not minor_id[0].isalpha():
                    minor_id = num1.split()[2]  # 大서가 처리
            except:
                minor_id = '확인불가'
            # TODO: shelf=find_shelf(major_id, minor_id); name, room_num, colrow = shelf.name, shelf.major_id, shelf.minor, shelf.row+shelf.col;
            shelf_list = Shelf.objects.filter(major_id__lte=major_id).exclude(room_num='1-1').exclude(room_num='7-1').order_by('major_id')
            if shelf_list.exists():
                shelf = shelf_list.last()
                room_num = shelf.room_num + '자료실'
                colrow = shelf.col + shelf.row
            else:
                room_num = '확인불가'
                colrow = ''
        info_list.append((name, major_id, minor_id, room_num, colrow, link))
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
