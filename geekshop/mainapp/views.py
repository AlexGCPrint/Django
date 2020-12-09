from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from django.conf import settings

from basketapp.models import Basket


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]
    content ={
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)


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
            'basket': basket
        }

        return render(request, "mainapp/products_list.html", content)

    same_products = Product.objects.all()

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
    }
    if pk:
        print(f"User select category: {pk}")

    return render(request, "mainapp/products.html", content)

def contact(request):
    title = 'Контакты'
    content ={
        'title': title
    }
    return render(request, 'mainapp/contact.html', content)