from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    # Select products that have been ordered and sort them by title
    # __in is lookups type
    query_set = Product.objects.filter(
        id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')

    return render(request, 'hello.html', {'name': 'Django Project', 'products': list(query_set)})