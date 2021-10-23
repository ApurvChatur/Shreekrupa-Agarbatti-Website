from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from ProjectDesign.models import (Home,
                                  Category,
                                  Product,
                                  )

def home_view(request):
    home = get_object_or_404(Home, title='Shreekrupa Agarbatti')
    categories = get_list_or_404(Category)
    featured_products = get_list_or_404(Product, tag='featured')

    template_name = 'ProjectModel/home-page.html'
    context = {
        'title': 'Home',
        'home': home,
        'categories': categories,
        'featured_products':featured_products,
    }
    return render(request, template_name, context)


def category_view(request, slug):
    categories = get_list_or_404(Category)
    category = get_object_or_404(Category, slug=slug)

    template_name = 'ProjectModel/category-page.html'
    context = {
        'title': category.title,
        'categories': categories,
        'category': category,
    }
    return render(request, template_name, context)


def products_view(request):
    categories = get_list_or_404(Category)
    products = Product.objects.all()

    template_name = 'ProjectModel/b-products-page.html'
    context = {
        'title': 'Products',
        'categories': categories,
        'products': products,
    }
    return render(request, template_name, context)


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectModel/c-product-page.html'
    context = {
        'title': product.title,
        'product': product,
    }
    return render(request, template_name, context)


def about_view(request):
    template_name = 'ProjectModel/d-about-page.html'
    context = {
        'title': 'About',
    }
    return render(request, template_name, context)


def contact_view(request):
    template_name = 'ProjectModel/e-contact-page.html'
    context = {
        'title': 'Contact',
    }
    return render(request, template_name, context)

