from urllib import request

import requests
from django.shortcuts import render
from .models import Diastrb



# Create your views here.
def dias_detail_view(request):
    # obj = Diastrb.objects.all()
    # m = request.POST.get("mes_sel")
    # print(m)
    id_mes = object = request.POST.get("id_mes")

    obj = Diastrb.objects.filter(mes=id_mes)

    t = 0
    for maydays in obj:

        if maydays.tipo == 1:
            t = t + 200
        else:
            t = t + 100

    # print(t)
    total = t
    context = {
        'object': obj,
        'total': total,
        'id_mes': id_mes
    }

    # print(context)
    return render(request, "dias/dias_details.html", context)
