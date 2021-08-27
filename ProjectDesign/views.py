from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import (Home,
                     Product,
                     ProductImage,
                     )
from .forms import (HomeForm,
                    ProductForm,
                    ProductImageForm,
                    )

# Entry
def entry_view(request):
    template_name = 'ProjectDesign/entry-page.html'
    context = {
        'title': 'Entry Page'
    }
    return render(request, template_name, context)


# Home Model (LCRUD)
# Home List
@staff_member_required()
def home_list_view(request):
    objects_list = Home.objects.all()

    template_name = 'ProjectDesign/Home/a-home-list-page.html'
    context = {
        'title': 'Home List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Home Create
@staff_member_required()
def home_create_view(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm()

    template_name = 'ProjectDesign/Home/b-home-create-page.html'
    context = {
        'title': 'Home Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Retrieve
@staff_member_required()
def home_retrieve_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/c-home-retrieve-page.html'
    context = {
        'title': 'Home Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Home Update
@staff_member_required()
def home_update_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm(instance=object)

    template_name = 'ProjectDesign/Home/d-home-update-page.html'
    context = {
        'title': 'Home Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Delete
@staff_member_required()
def home_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Home, slug=slug)
        object.delete()
        return redirect('ProjectDesign:home-list-page')
    else:
        object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/e-home-delete-page.html'
    context = {
        'title': 'Home Delete',
        'object': object,
    }
    return render(request, template_name, context)


# Product Model (LCRUD)
# Product List
@staff_member_required()
def product_list_view(request):
    objects_list = Product.objects.all()

    template_name = 'ProjectDesign/Product/a-product-list-page.html'
    context = {
        'title': 'Product List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Product Create
@staff_member_required()
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-list-page')
    else:
        form = ProductForm()

    template_name = 'ProjectDesign/Product/b-product-create-page.html'
    context = {
        'title': 'Product Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Product Retrieve
@staff_member_required()
def product_retrieve_view(request, slug):
    object = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectDesign/Product/c-product-retrieve-page.html'
    context = {
        'title': 'Product Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Product Update
@staff_member_required()
def product_update_view(request, slug):
    object = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-list-page')
    else:
        form = ProductForm(instance=object)

    template_name = 'ProjectDesign/Product/d-product-update-page.html'
    context = {
        'title': 'Product Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Product Delete
@staff_member_required()
def product_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Product, slug=slug)
        object.delete()
        return redirect('ProjectDesign:product-list-page')
    else:
        object = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectDesign/Product/e-product-delete-page.html'
    context = {
        'title': 'Product Delete',
        'object': object,
    }
    return render(request, template_name, context)


# ProductImage Model (LCRUD)
# ProductImage List
@staff_member_required()
def product_image_list_view(request):
    objects_list = ProductImage.objects.all()

    template_name = 'ProjectDesign/ProductImage/a-product-image-list-page.html'
    context = {
        'title': 'Product Image List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# ProductImage Create
@staff_member_required()
def product_image_create_view(request):
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-image-list-page')
    else:
        form = ProductImageForm()

    template_name = 'ProjectDesign/ProductImage/b-product-image-create-page.html'
    context = {
        'title': 'Product Image Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# ProductImage Retrieve
@staff_member_required()
def product_image_retrieve_view(request, slug):
    object = get_object_or_404(ProductImage, slug=slug)

    template_name = 'ProjectDesign/ProductImage/c-product-image-retrieve-page.html'
    context = {
        'title': 'Product Image Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# ProductImage Update
@staff_member_required()
def product_image_update_view(request, slug):
    object = get_object_or_404(ProductImage, slug=slug)

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:product-image-list-page')
    else:
        form = ProductImageForm(instance=object)

    template_name = 'ProjectDesign/ProductImage/d-product-image-update-page.html'
    context = {
        'title': 'Product Image Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# ProductImage Delete
@staff_member_required()
def product_image_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(ProductImage, slug=slug)
        object.delete()
        return redirect('ProjectDesign:product-image-list-page')
    else:
        object = get_object_or_404(ProductImage, slug=slug)

    template_name = 'ProjectDesign/ProductImage/e-product-image-delete-page.html'
    context = {
        'title': 'Product Image Delete',
        'object': object,
    }
    return render(request, template_name, context)


