from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'curso': 'Programação WEB com DJANGO FRAMEWORK.',
        'products': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    # products = Product.objects.get(id=pk)
    products = get_object_or_404(Product, id=pk)

    context = {
        'product': products
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404)