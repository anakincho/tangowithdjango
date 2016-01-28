from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('Rango says hey there world! <br /> <a href="/rango/about">About</a>')
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)
def about(request):
    return HttpResponse('Rango decided that this will be the about page! <br /><a href="/rango/" style="color: orange; text-decoration:none;font-family:Verdana;border: 1px solid black; border-radius: 5px;padding: auto; background-color: black;"><-Go back</a>')