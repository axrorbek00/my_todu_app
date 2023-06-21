from django.shortcuts import render, redirect
from .forms import CreateToduFormsModel
from .forms import ToduModel


def todu_list_view(request):
    tasks = ToduModel.objects.all()
    return render(request, 'main/todu_list.html', context={
        'tasks': tasks
    })


def todu_create_view(request):
    form = CreateToduFormsModel()
    if request.method == 'POST':
        form = CreateToduFormsModel(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todu_list')

    return render(request, 'main/todu_create.html', context={
        'create_form': form
    })
