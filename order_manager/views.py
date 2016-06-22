from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAccount, Price, Product, Dispensary, Order
from .forms import ProductForm
from django.utils import timezone


@login_required
def home(request):
    """
    A log_in is needed to verify user id and continue to Home.
    Sign in with user name and password.
    If valid you will see an awesome gif_pic and a Menu option.
    User will click Menu and be taken to the Menu page.
    There is a link at the bottom of the page crediting the Gif artist that will take user to their site when clicked on.
    """
    form = AuthenticationForm()
    return render(request, 'order_manager/home.html', {
        'form': form
    })


def product_menu(request):
    """
    Product menu displays a list of all cannabis strains available in alphabetical order, a description of each strain, strain prices, and weights offered.
    User selects which product(s) they want to purchase and when ready click the Submit button at the bottom of the page which directs them to the Product_Confirmation page.
    """
    products = Product.objects.all().order_by('strain')
    return render(request, 'order_manager/menu.html', {
        'products': products
    })


def product_confirmation(request):
    """
    This is the users order confirmation page that lets the user know that the order was successfully processed with a message receipt back to them.
    It also has a link back to the Homepage.
    """
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.time_pickup = ()
            order.save()
        return render(request, 'order_manager/confirmation.html')
    else:
        return render(request, 'order_manager/menu.html', {'form': form})


def product_item(request, id):
    """
    Product_item was simply created for testing purposes only, though it is able to be pulled up if URL product/and a # of item/ is entered in the address bar.
    If pulled up it renders a simple view of the product that correlates to the # entered, it's description, and price/weight offered on that strain.
    """
    return render(request, 'order_manager/item.html', {
        'item': Product.objects.get(pk=id)
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
