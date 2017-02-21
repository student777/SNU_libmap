from django.shortcuts import render
from shelf_map.search import search_title


def index(request):
    if request.GET.get('title'):
        title = request.GET.get('title')
        info_list = search_title(title)
        return render(request, 'index.html', {'info_list': info_list, })
    else:
        return render(request, 'index.html')
