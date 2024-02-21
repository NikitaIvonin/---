from django.shortcuts import render
from .models import *

# Create your views here.
def build_template(lst: list, cols: int) -> list[list]:
    new_list = []
    for i in range(0, len(lst), cols):
        new_list.append(lst[i:i + cols])
    return new_list

build_template([1,2,3,4,5,6,7,8,9,10], 3)

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'auto_store/product_list.html', context={
                                                                    'product_list': build_template(products, 3),
                                                                    'categories': categories,
                                                                    })


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)
    return render(request, 'auto_store/product_detail.html', context={'product': product, 'categories': categories})