from django.shortcuts import render
from shelf_map.search import search_title
from shelf_map.models import Shelf
from django.http import Http404


def index(request):
    if request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        if Shelf.objects.filter(major_id=major_id).count() > 1:
            minor_id = request.GET.get('minor_id')
            result = Shelf.objects.filter(major_id=major_id, minor_id__lte=minor_id).order_by('minor_id').last()
        else:
            result = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id').last()
        if result is None:
            raise Http404('검색 불가. 0~999 사이의 숫자를 입력해 주세요. 7열람실 서가는 모름')
        return render(request, 'index.html', {'result': result, })
    elif request.GET.get('title'):
        title = request.GET.get('title')
        info_list = search_title(title)
        return render(request, 'index.html', {'info_list': info_list, })
    else:
        return render(request, 'index.html')
