from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    query_set = Product.objects.order_by('title') # asc
    #query_set = Product.objects.order_by('-title') -> desc

    query_set = Product.objects.order_by('unit_price', '-title')

    product = Product.objects.order_by('unit_price')[0] # First product after sorting
    product = Product.objects.earliest('unit_price') # First product

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})