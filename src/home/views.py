from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit 

this_dir = pathlib.Path(__file__).resolve().parent

#VIEWS
def home_view(request, *args, **kwargs):#args: let function take an unknown number of positional arguments, stores them as a tuple.  **\\kwargs* let it take an unknown number of keyword arguments, stores them as a dictionary. useful when you don’t know ahead of time how many values will be passed into your function.
    return about_view(request,*args, **kwargs )


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all() #db object returns all logged visits 
    page_qs = PageVisit.objects.filter(path=request.path) #returns logged visits for this particular path
    my_title = "Tobi"
    try:
        percent = round(((page_qs.count()/qs.count())*100),2)
    except ZeroDivisionError:
        percent = 0
    my_context = {
        "page_title":my_title,
        "queryset" : qs, 
        "page_visit_count": page_qs.count, #how many times have i been to all pages 
        "total_visit_count": qs.count(), #how many times have i been to this page 
        "visits_on_this_page": percent


    }
    
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)#add a row to model everytime a page is visited, include the path visited
    return render(request, html_template, my_context)

 