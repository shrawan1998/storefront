from django.shortcuts import render
from django.db.models import Q
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    # Products: inventory < 10 AND price < 20
    query_set = Product.objects.filter(inventory__lt = 10, unit_price__lt = 20)

    # chaining the filter method
    query_set = Product.objects.filter(inventory__lt = 10).filter(unit_price__lt = 20)

    # Products: inventory < 10 OR price < 20
    query_set = Product.objects.filter(Q(inventory__lt = 10) | Q(unit_price__lt = 20))

    #query_set = Product.objects.filter(Q(inventory__lt = 10) & ~Q(unit_price__lt = 20))

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})