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
    # gt_3_item = MoviesInfo.objects.filter()
    queryset = MoviesInfo.objects.values('grade')
    condtions = {'grade__gte': 3}

    gt_3_item = queryset.filter(**condtions).count()
    short = queryset.filter(**condtions)
    grade = queryset.filter(**condtions)

    return render(request, 'showMovies.html', locals())
