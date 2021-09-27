from django.shortcuts import render
from ProjectDesign.models import (Home,
                                  Product,
                                  )

def home_view(request):
    home = Home.objects.all()
    products = Product.objects.all()

    template_name = "ProjectReal/home-page.html"
    context = {
        'home': home,
        'products': products,

    }
    return render(request, template_name, context)
