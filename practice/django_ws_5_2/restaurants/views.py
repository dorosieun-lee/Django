from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }

    return render(request, 'restaurants/index.html', context)

def detail(request, pk):
    item = Restaurant.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'restaurants/detail.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')

    item = Restaurant(name=name, description=description, address=address, phone_number=phone_number)
    item.save()

    return redirect('restaurants:index')

def edit(request, pk):
    item = Restaurant.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'restaurants/edit.html', context)

def update(request, pk):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    item = Restaurant(name=name, description=description, address=address, phone_number=phone_number)
    item.save()
    
    return redirect('restaurants:index')

def delete(request, pk):
    item = Restaurant.objects.get(pk=pk)
    item.delete()
    return redirect('restaurants:index')