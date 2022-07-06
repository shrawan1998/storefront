from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    #Products: inventory = price
    # F() -> constructor of F class
    query_set = Product.objects.filter(inventory = F('unit_price'))

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})