from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    # Reading a related field which is collection in Product class
    # It will create a query to inner join query
    # values() return dict objects instead of Product objects
    query_set = Product.objects.values('id', 'title', 'collection__title')

    # values_list() return tuple object
    query_set = Product.objects.values_list('id', 'title', 'collection__title')

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})