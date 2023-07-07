from django.shortcuts import render, redirect
from .forms import CreateToduFormsModel, EditToduModelForm
from .forms import ToduModel
from django.contrib.auth.decorators import login_required


def home_wiuv(request):
    return render(request, 'main/home_page.html')


def todu_check_viuw(request, id):
    obj = ToduModel.objects.all().get(id=id)
    if obj.task_status:
        obj.task_status = False
    else:
        obj.task_status = True
    obj.save()
    return redirect('todu_list')


@login_required
def todu_edit_view(request, id):
    obj = ToduModel.objects.all().get(id=id)
    if request.method == 'POST':
        form = EditToduModelForm(data=request.POST)
        if form.is_valid():
            obj.task_name = form.cleaned_data['task_name']
            obj.description = form.cleaned_data['description']
            obj.save()
            return redirect('todu_list')
    return render(request, 'main/todu_edit.html', context={
        'task': obj
    })


@login_required
def todu_detail_view(request, id):
    obj = ToduModel.objects.all().get(id=id)
    text = '800-COLLECT'
    return render(request, 'main/my_todu_datail.html', context={
        'task': obj,
        'text': text,
    })


@login_required
def todu_delete_view(request, id):
    ToduModel.objects.all().filter(id=id).delete()
    return redirect('todu_list')


@login_required
def todu_list_view(request):
    q = request.GET.get('q', '')
    tasks = ToduModel.objects.all().filter(user=request.user)
    if q:
        tasks = tasks.filter(task_name__icontains=q)
    return render(request, 'main/todu_list.html', context={
        'tasks': tasks,
        'q': q
    })


@login_required
def todu_create_view(request):
    form = CreateToduFormsModel()
    if request.method == 'POST':
        form = CreateToduFormsModel(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('todu_list')
    return render(request, 'main/todu_create.html', context={
        'create_form': form
    })
