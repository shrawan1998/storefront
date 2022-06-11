from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view -> request handler
# request -> response
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Django Project'})