from genericpath import exists
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    exists = Product.objects.filter(pk=0).exists()
    # Return type of exists method is boolean
    # pk stands for primary key

    query_set = Product.objects.filter(unit_price__range = (20, 30))
    # filtering the products which have unit price in range(20, 30)
    #unit_price__gt = 20 --> Field lookups

    #query_set = Product.objects.all()
    # Product.objects gives us a manager (interface to the db)
    # all() always return query set. It dosen't return object.
    # To get object we need to iterte the query set
    #list(query_set)

    count = Product.objects.count()
    # Return actual object instead of query set

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})