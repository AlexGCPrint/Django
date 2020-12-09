from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.conf import settings


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]
    content ={
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
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