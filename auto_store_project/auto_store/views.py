from django.shortcuts import render
from .models import Product

# Create your views here.
def build_template(lst: list, cols: int) -> list[list]:
    new_list = []
    for i in range(0, len(lst), cols):
        new_list.append(lst[i:i + cols])
    return new_list

build_template([1,2,3,4,5,6,7,8,9,10], 3)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'auto_store/product_list.html', context={'product_list': build_template(products, 3)})
