from django.shortcuts import render, redirect
from .forms import CreateToduFormsModel, EditToduModelForm
from .forms import ToduModel


def todu_edit_view(request, id):
    obj = ToduModel.objects.all().get(id=id)
    if request.method == 'POST':
        form = EditToduModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todu_list')
    return render(request, 'main/todu_edit.html', context={
        'task': obj
    })


def todu_detail_view(request, id):
    obj = ToduModel.objects.all().get(id=id)
    return render(request, 'main/my_todu_datail.html', context={
        'task': obj
    })


def todu_delete_view(request, id):
    ToduModel.objects.all().filter(id=id).delete()
    return redirect('todu_list')


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
