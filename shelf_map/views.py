from django.shortcuts import render
from django.http import HttpResponse  #NQOA
from shelf_map.models import Shelf


def index(request):
    if request.GET.get('major_id'):
        major_id = request.GET.get('major_id')
        minor_id = request.GET.get('minor_id')
        result =  Shelf.objects.filter(major_id__lte=major_id).order_by('major_id').last()
        return render(request, 'index.html', {'result': result})
    # result = ''
    # return HttpResponse(result)
    shelfs = Shelf.objects.all()
    return render(request, 'index.html', {'shelfs': shelfs})
