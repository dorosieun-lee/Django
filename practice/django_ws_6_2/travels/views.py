from django.shortcuts import render, redirect
from django.http import Http404
from .form import TravelForm
from .models import Travel

app_name = 'travels'
# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context = {
        "travels": travels,
    }
    return render(request, 'travels/index.html', context)


def detail(request, pk):
    try:
        item = Travel.objects.get(pk=pk)
    except Travel.DoesNotExist:
        raise Http404('존재하지 않는 페이지입니다.')
    context = {
        "item": item,
    }
    return render(request, 'travels/detail.html', context)


def create(request):
    if request.method == "POST":
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect("travels:detail", travel.pk)
    else:
        form = TravelForm()

    context = {
        "form": form,
    } 
    return render(request, 'travels/create.html', context)

