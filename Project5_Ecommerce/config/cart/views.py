from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddProductFrom
from .cart import Cart
from coupon.forms import AddCouponForm

# Create your views here.
@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductFrom(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])
    
    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')

# detail(): 장바구니 페이지
def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()

    for product in cart:
        product['quantity_form'] = AddProductFrom(initial={'quantity': product['quantity'], 'is_update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'add_coupon': add_coupon})