from django.shortcuts import render, redirect
from .forms import ContactForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Вывод данных формы в консоль (требование задания 4.9)
            print(f"Обратная связь: {name} ({email}): {message}")
            # Перенаправление на главную после успешной отправки
            return redirect('homepage:index_page')
    else:
        form = ContactForm()

    return render(request, 'homepage/contacts.html', {'form': form})