from django.shortcuts import render
from .models import Diastrb


# Create your views here.
def dias_detail_view(request):
    obj = Diastrb.objects.all()
    t = 0
    for maydays in obj:
        if maydays.tipo == 1:
            t = t + 200
        else:
            t = t + 100
    #print(t)
    total = t
    context = {
        'object': obj,
        'total': total
    }

    # print(context)
    return render(request, "dias/dias_details.html", context)
