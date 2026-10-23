from django.shortcuts import render
from django.http import HttpResponse


def product_list(request):
    products = [
        {
            'title': 'Овсянка «Здоровье»',
            'description': 'Цельнозерновая овсяная крупа холодной обработки, '
                           'богата клетчаткой, идеальна для полезного завтрака.',
        },
        {
            'title': 'Яблоки «Антоновка»',
            'description': 'Свежие садовые яблоки с кислинкой, выращены без '
                           'пестицидов, отлично подходят для выпечки и соков.',
        },
        {
            'title': 'Грецкие орехи',
            'description': 'Очищенные грецкие орехи, источник омега-3, '
                           'полезны для сердца и мозга, хранятся в вакуумной упаковке.',
        },
        {
            'title': 'Мёд «Разнотравье»',
            'description': 'Натуральный цветочный мёд с пасеки в Алтайском крае, '
                           'без добавок и сахара, обладает антибактериальными свойствами.',
        },
    ]

    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    return render(request, 'catalog/product_detail.html', context={'pk': pk})