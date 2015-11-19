from django.shortcuts import render
from shelf_map.models import Shelf
from shelf_map.search import search


def index(request):
    if request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        # minor_id = request.GET.get('minor_id')
        result = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id').last()
        if result is None:
            result = '검색 결과가 없습니다(DB 더 채워야함)'
        return render(request, 'index.html', {'result': result})
    elif request.GET.get('title'):
        title = request.GET.get('title')
        result_msg = search(title)
        return render(request, 'index.html', {'result_msg': result_msg})
    else:
        return render(request, 'index.html')


def list(request):
    list = Shelf.objects.all()
    return render(request, 'list.html', {'list': list})