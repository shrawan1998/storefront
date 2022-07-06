from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    try:
        product = Product.objects.get(pk=0)
        # pk stands for primary key
    except ObjectDoesNotExist as e:
        print(e)

    query_set = Product.objects.all()
    # Product.objects gives us a manager (interface to the db)
    # all method always return query set. It dosen't return object.
    # To get object we need to iterte the query set
    # for product in query_set:
    #     print(product)
    list(query_set)

    count = Product.objects.count()
    # Return actual object instead of query set

    return render(request, 'hello.html', {'name': 'Django Project'})