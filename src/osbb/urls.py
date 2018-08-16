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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view
from pages.views import post_detail_view, new_post_view, post_edit_view, post_delete
from pages.views import contact_view, information_view, regulations_view
from pages.views import login_view, logout_view, registration_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('home/', home_view, name='home'),
    path('contacts/', contact_view, name='contacts'),
    path('information/', information_view, name='information'),
    path('regulations/', regulations_view, name= 'regulations'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/new/', new_post_view, name='post_new'),
    path('post/<int:pk>/edit/', post_edit_view, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)