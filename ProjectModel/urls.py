from django.urls import path
from .views import (home_view,
                    products_view,
                    product_view,
                    about_view,
                    contact_view)

app_name = 'ProjctModel'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('products/', products_view, name='products-page'),
    path('product/<slug:slug>', product_view, name='product-page'),
    path('about/', about_view, name='about-page'),
    path('contact/', contact_view, name='contact-page'),
]
