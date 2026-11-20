from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import OrderForm


def product_list(request):
    products = Product.objects.filter(is_available=True)
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Вывод данных заказа в консоль (требование лабораторной)
            print(
                f"Новый заказ: {order.customer_name}, "
                f"тел. {order.phone}, "
                f"товар «{order.product.title}», "
                f"кол-во: {order.quantity}"
            )
            return redirect('homepage:index_page')
    else:
        form = OrderForm(initial={'product': product})

    context = {'product': product, 'form': form}
    return render(request, 'catalog/product_detail.html', context)