

from django.http import HttpResponse
from django.shortcuts import render


#create your views here.


def home_view(request=None, *args, **kwargs):

    my_context = dict(my_text="This is about DJANGO", my_number="12345678910", my_dog="Shao Khan", my_list=[123, 232, 2333322, 33, 'ABC'])
    print(my_context)
    print(args, kwargs)
    #return HttpResponse("<h1 style='color:blue;'>Teste Home</h1>")
    return render(request, 'home.html', my_context)

def dogz_view(*args, **kwargs):
    return HttpResponse("<h1>Knockout Shao Khan LSDogz </h1><br><p> <br >Offspring: none <br Breedings: none <br> Siblings: noneGeneral InformationCurrent Owner: Abr VanelliRegistration Name: Knockout Shao Khan</p>")

def dias_trb(request=None, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1 style='color:blue;'>Teste Home</h1>")
    return render(request, 'dias.html',{})