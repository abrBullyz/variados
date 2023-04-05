from django.shortcuts import render
# from forms import DogzForm
from .models import Dogz


# Create your views here.
# def dog_create_view(request):
#     form = DogzForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     # obj = Dogz.objects.get(id=1)
#     # obj = Dogz.objects.all()
#
#     # context = {
#     #     'nome': obj.nome,
#     #     'raca': obj.raca,
#     #     'obs': obj.obs,
#     #     'site':obj.site,
#     #
#     #
#     # }
#
#     context = {
#         'form': form
#     }

    # return render(request, "dogz/dogz_detail.html", context)

def dogz_detail_view(request):
    # obj = Dogz.objects.get(id=1)
    obj = Dogz.objects.all()

    # context = {
    #     'nome': obj.nome,
    #     'raca': obj.raca,
    #     'obs': obj.obs,
    #     'site':obj.site,
    #
    #
    # }

    context = {
        'object': obj
    }


   # print(context)
    return render(request, "dogz/detail.html", context)

