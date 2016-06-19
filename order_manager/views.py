from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount, Price, Product, Dispensary, Order
# from .forms import OrderForm
from django.utils import timezone


@login_required
def home(request):
    form = AuthenticationForm()
    return render(request, 'order_manager/home.html', {
        'form': form
    })


def product_menu(request):
    products = Product.objects.all().order_by('strain')
    return render(request, 'order_manager/menu.html', {
        'products': products
    })


# def order_form(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.time_pickup = ()
#             order.save()
#         return render(request, 'order_manager/confirmation.html')
#     else:
#         form = OrderForm()
#     return render(request, 'order_manager/order.html', {'form': form})


def product_item(request, id):
    return render(request, 'order_manager/item.html', {
        'item': Product.objects.get(pk=id)
    })


def product_confirmation(request):
    if request.method == "POST":
        confirmation = Product.objects.get(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.time_pickup = ()
            order.save()
        return render(request, 'order_manager/confirmation.html')
    else:
        return render(request, 'order_manager/menu.html')
