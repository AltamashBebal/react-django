"""ReactDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from authapp.views import index
from authapp import views
from Product import views as ProductView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('user/delete/<str:user_name>/', views.delete),
    path('user/getAll/', views.getUsers),
    path('user/<str:username>/', views.getUser),
    path('products/getAll/', ProductView.getProducts),
    path('products/delete/<str:pk>', ProductView.deleteProduct),
    path('products/addProduct/', ProductView.addProduct),
    path('products/addProductForCustomer/', ProductView.addProductForCustomer),
    path('products/getCustomerWise/<str:cname>', ProductView.getCustomerWise)
    # path('auth/', include(authapp.urls))
]
