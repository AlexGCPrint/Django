from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from django.conf import settings
import datetime
import random

from basketapp.models import Basket

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []

def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]

def get_same_products(hot_product):
    return Product.objects.filter(category__pk=hot_product.category.pk).exclude(pk=hot_product.pk)[:3]


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]
    content ={
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        content = {
            'title': title,
            "links_menu": links_menu,
            'products': products_list,
            'category': category,
            'basket': basket,
            'hot_product': get_hot_product(),
        }

        return render(request, "mainapp/products_list.html", content)

    hot_product = get_hot_product()

    same_products = get_same_products(hot_product)

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        'basket': basket,
        'hot_product': get_hot_product(),
    }
    if pk:
        print(f"User select category: {pk}")

    return render(request, "mainapp/products.html", content)

def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request,  "mainapp/product.html", content)

def contact(request):
    title = 'Контакты'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'adress': 'Близко к океану',
        },
    ]
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)