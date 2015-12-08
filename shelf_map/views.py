from django.shortcuts import render
from shelf_map.search import search_title
from shelf_map.models import Shelf
from django.http import Http404


def index(request):
    if request.GET.get('title'):
        title = request.GET.get('title')
        info_list = search_title(title)
        return render(request, 'index.html', {'info_list': info_list, })
    elif request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        try:
            Shelf.objects.filter(major_id=major_id)
        except:
            raise Http404('검색 결과가 없습니다. 0~999 범위의 값을 입력해 주세요')
            
        if Shelf.objects.filter(major_id=major_id, major_leadingChr=None).exclude(room_num='1-1').exclude(room_num='7-1').count() > 1:
            minor_id = request.GET.get('minor_id')
            if minor_id is '':
                result = Shelf.objects.filter(major_id=major_id, major_leadingChr=None).exclude(room_num='1-1').exclude(room_num='7-1').first()
                # alert message: minor_id is required 
            else:
                result = Shelf.objects.filter(major_id=major_id, minor_id__lte=minor_id, major_leadingChr=None).exclude(room_num='7-1').exclude(room_num='1-1').order_by('minor_id').last()
        else:
            result = Shelf.objects.filter(major_id__lte=major_id, major_leadingChr=None).exclude(room_num='7-1').exclude(room_num='1-1').order_by('major_id').last()
        if result is None: 
            raise Http404('검색 오류. 0~999 범위의 값을 입력해 주세요')
        return render(request, 'index.html', {'result': result, })

    else:
        return render(request, 'index.html')
