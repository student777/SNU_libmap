from django.shortcuts import render
from shelf_map.search import search_title, search_shelf
from django.http import Http404


def index(request):
    if request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        try:
            Shelf = search_shelf(float(major_id))
        except ValueError:
            raise Http404('大도서, A나 K로 시작하는 도서 검색은 준비중입니다.')
        if Shelf.objects.filter(major_id=major_id).count() > 1:
            minor_id = request.GET.get('minor_id')
            result = Shelf.objects.filter(major_id=major_id, minor_id__lte=minor_id).order_by('minor_id').last()
        else:
            result = Shelf.objects.filter(major_id__lte=major_id).order_by('major_id').last()
        return render(request, 'index.html', {'result': result, 'shelf_num': result.__class__.__name__, })
    elif request.GET.get('title'):
        title = request.GET.get('title')
        info_list = search_title(title)
        return render(request, 'index.html', {'info_list': info_list, })
    else:
        return render(request, 'index.html')


