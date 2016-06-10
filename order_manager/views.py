from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount, Price, Product, Dispensary, Order
from .forms import OrderForm
from django.utils import timezone


@login_required
def product_item(request, id):
    return render(request, 'order_manager/item.html', {
        'item': Product.objects.get(pk=id)
    })


def product_list(request):
    products = Product.objects.all()
    return render(request, 'order_manager/list.html', {
        'products': products
    })


def order_form(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.time_pickup = ()
            order.save()
        return redirect('product_item', id=product.pk)
    else:
        form = OrderForm()
    return render(request, 'order_manager/order.html', {'form': form})


def home(request):
    products = Product.objects.all()
    form = AuthenticationForm()
    return render(request, 'order_manager/home.html', {
        'products': products,
        'form': form
    })
