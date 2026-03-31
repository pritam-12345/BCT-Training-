from django.shortcuts import render
from .models import Product

# Create your views here.
def app(request):
    products=Product.objects.all()
    return render(request,"newApp/app.html",{'products':products})
def about(request):
    return render(request,"newApp/about.html")
