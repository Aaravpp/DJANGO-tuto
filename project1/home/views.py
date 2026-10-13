from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(Request):
    return HttpResponse("Welcome to Django!")

def products(request):
    product_list = ["Laptop", "Mobile", "TV", "Keyboards", "Monitor"]

    return render(
        request,
        "products.html",
        {"products": product_list}
    )

def product_details(request, product_id):
    return HttpResponse(f"Product id : {product_id}")