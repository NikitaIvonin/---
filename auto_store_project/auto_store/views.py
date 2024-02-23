from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin
from django.http import HttpResponse

# Create your views here.


def work(request):
    #p = Product(title='Range Rover', price=20000)
    #p.save()

   # Product.objects.create(title = "Hundai", price=25000)

   # obj = Product.objects.get(title='BMW')
    
    
    
    obj = Product.objects.all().order_by('pk')

   # obj = Product.objects.all()
   # print(obj.price)
    return HttpResponse('Hello')


class HomeView(ListView, CategoriesMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
                |
                Q(price__icontains=search_query)
            )
        return Product.objects.all()
    
    

class ProductView(DetailView, CategoriesMixin):
    model = Product



class CategoryView(DetailView, CategoriesMixin):
    model = Category

    
def save_order(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()
    return render(request, 'auto_store/order.html', context={
                                                                    'product_list': build_template(products, 3),
                                                                    'categories': categories,
                                                                    'order': order
                                                                    })