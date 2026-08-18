from django.http import HttpResponse

#VIEWS
def home_page(request, *args, **kwargs):#args: let function take an unknown number of positional arguments, stores them as a tuple.  **\\kwargs* let it take an unknown number of keyword arguments, stores them as a dictionary. useful when you don’t know ahead of time how many values will be passed into your function.

    return HttpResponse("<h1> Hello World</h1>")