from django.shortcuts import render


def todu_list_view(request):
    return render(request, 'main/todu_list.html')
