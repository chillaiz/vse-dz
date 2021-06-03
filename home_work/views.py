from django.http import HttpResponse
from django.shortcuts import render, redirect

from djangoProject3.forms import CategoryForm
from home_work.models import Product, Review, Category


# Create your views here.


def get_all_product(request):
    word = (request.GET.get('search', ''))
    productes = Product.objects.filter(title__contains=word)

    data = {
        'all_productes': productes
    }

    for i in range(len(data['all_productes'])):
        reviews = Review.objects.filter(products_id=data['all_productes'][i].id)
        data['all_productes'][i].col = len(reviews)

    return render(request, 'productes.html', context=data)


def get_one_product(request, id):
    produc = Product.objects.get(id=id)
    rewiev = Review.objects.filter(products_id=id)
    data = {
        'produc': produc,
        'rewiev': rewiev
    }
    return render(request, 'detail.html', context=data)


def add(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            Category.objects.create(name=name)
            return redirect('/product/')
        else:
            return render(request, 'add1.html', context={
                'form': form
            })
    data = {
        'form': CategoryForm()
    }
    return render(request, 'add1.html', context=data)