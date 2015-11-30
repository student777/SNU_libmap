from django.shortcuts import render
from shelf_map.search import search_title, search_shelf
from shelf_map.models import Shelf_1


def index(request):
    if request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        Shelf = search_shelf(major_id)
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


def list(request):
    list = Shelf_1.objects.all()
    return render(request, 'list.html', {'list': list})
