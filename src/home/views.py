from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

#VIEWS
def home_page(request, *args, **kwargs):#args: let function take an unknown number of positional arguments, stores them as a tuple.  **\\kwargs* let it take an unknown number of keyword arguments, stores them as a dictionary. useful when you don’t know ahead of time how many values will be passed into your function.
    my_title = "Tobi"
    my_context = {
        "page_title":my_title,
    }
    html_template = "home.html"
    return render(request, html_template, my_context)


def home_page_old(request, *args, **kwargs):#args: let function take an unknown number of positional arguments, stores them as a tuple.  **\\kwargs* let it take an unknown number of keyword arguments, stores them as a dictionary. useful when you don’t know ahead of time how many values will be passed into your function.
    my_title = "Tobi"
     
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_) 