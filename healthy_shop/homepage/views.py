from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_page(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse('Описание проекта «Магазин правильных продуктов»')

def contacts(request):
    return render(request, 'homepage/contacts.html')