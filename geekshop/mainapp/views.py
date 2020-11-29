from django.shortcuts import render

# Create your views here.

def main(request):
    content ={
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    content ={
        'title': 'Продукты'
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    content ={
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)