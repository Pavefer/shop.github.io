from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.response import TemplateResponse

from .models import *
from django.db.models import Q
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query))

    else:
        if category_slug != None:
            category_page = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category_page, available=True)
        else:
            products = Product.objects.all().filter(available=True)

    category_page = None

    return render(request,
                  'shop/product/list.html',
                  {'category': category_page, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def aboutus(request):
    return render(request, 'shop/aboutus.html')


def contact(request):
    return render(request, 'shop/contact.html')
