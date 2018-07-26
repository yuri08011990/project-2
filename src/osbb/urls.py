"""osbb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from pages.views import post_detail_view
from pages.views import new_post_view
from pages.views import post_edit_view
from pages.views import contact_view, information_view, regulations_view
from products.views import product_detail_view
from products.views import product_create_view
from products.views import render_initial_data
from products.views import dynamic_lookup_view
from products.views import product_delete_view
from products.views import product_list_view
# from blog.views import post_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('contacts/', contact_view, name='contacts'),
    path('information/', information_view, name='information'),
    path('regulations/', regulations_view, name= 'regulations'),
    path('create/', product_create_view,),
    path('product/', product_detail_view),
    path('products/<int:id>/', dynamic_lookup_view, name='product'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('products/', product_list_view, name='product-list'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/new/', new_post_view, name='post_new'),
    path('post/<int:pk>/edit/', post_edit_view, name='post_edit'),
]
