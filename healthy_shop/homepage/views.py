from django.shortcuts import render
from django.http import HttpResponse

def index_page(request):
    template_name = 'homepage/index.html'
    title = 'Главная страница «Магазин правильных продуктов»'
    promo_product = 'Овсянка «Здоровье»'

    context = {
        'title': title,
        'promo_product': promo_product,
    }
    return render(request, template_name, context)

def about(request):
    return render(request, 'homepage/about.html')

def contacts(request):
    return render(request, 'homepage/contacts.html')