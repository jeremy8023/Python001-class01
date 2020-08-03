from django.shortcuts import render
from django.http import HttpResponse
from .models import MoviesInfo
from django.db.models import F

# Create your views here.
def test(request,):
    i = 100
    return render(request, 'test.html', locals())

def show_movies(request,):
    count_movies_item = MoviesInfo.objects.all().count()
    gt_3_item_counter = MoviesInfo.objects.filter(grade__gt=3).count()
    # shorts = MoviesInfo.objects.filter(grade__gte='3')[:10]

    queryset = MoviesInfo.objects.values('grade')
    condtions = {'grade__gt': 3}
    gt_3_item_counter = queryset.filter(**condtions).count()
    
    q1 = queryset.filter(**condtions)
    
    items = []
    # v是一个字典，存储的数据库的内容
    for v in q1.values():
        items.append(v)
    
    shorts = []
    grades = []
    # 遍历items
    for i in items:
        shorts.append(i['short'])
        grades.append(i['grade'])


    
    # grades = queryset.filter(**condtions)

    return render(request, 'showMovies.html', locals())
