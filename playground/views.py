from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    # 0, 1, 2, 3, 4 -> limit: 5
    query_set = Product.objects.all()[:5]

    # 5, 6, 7, 8, 9 -> limit: 5, offset: 5 (for skipping first 5 elements)
    query_set = Product.objects.all()[5:10]

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})