from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    return render(request, 'catalog/product_list.html')


def product_detail(request, pk):
    return render(request, 'catalog/product_detail.html', context={'pk': pk})