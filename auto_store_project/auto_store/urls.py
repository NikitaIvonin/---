"""
URL configuration for auto_store_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import HomeView, ProductView, CategoryView, save_order, work
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_detail_url'),
    path('save_order', save_order),
]