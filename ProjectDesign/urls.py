from django.urls import path
from .views import (entry_view,

                    # Home Model
                    home_list_view,
                    home_create_view,
                    home_retrieve_view,
                    home_update_view,
                    home_delete_view,

                    # Product Model
                    product_list_view,
                    product_create_view,
                    product_retrieve_view,
                    product_update_view,
                    product_delete_view,

                    # Product Image Model
                    product_image_list_view,
                    product_image_create_view,
                    product_image_retrieve_view,
                    product_image_update_view,
                    product_image_delete_view,
                    )

app_name = 'ProjectDesign'

urlpatterns = [
    # Entry
    path('', entry_view, name='entry-page'),

    # Home Model
    path('home-list-page/', home_list_view, name='home-list-page'),
    path('home-create-page/', home_create_view, name='home-create-page'),
    path('home-retrieve-page/<slug>/', home_retrieve_view, name='home-retrieve-page'),
    path('home-update-page/<slug>/', home_update_view, name='home-update-page'),
    path('home-delete-page/<slug>/', home_delete_view, name='home-delete-page'),

    # Product Model
    path('product-list-page/', product_list_view, name='product-list-page'),
    path('product-create-page/', product_create_view, name='product-create-page'),
    path('product-retrieve-page/<slug>/', product_retrieve_view, name='product-retrieve-page'),
    path('product-update-page/<slug>/', product_update_view, name='product-update-page'),
    path('product-delete-page/<slug>/', product_delete_view, name='product-delete-page'),

    # Product Image Model
    path('product-image-list-page/', product_image_list_view, name='product-image-list-page'),
    path('product-image-create-page/', product_image_create_view, name='product-image-create-page'),
    path('product-image-retrieve-page/<slug>/', product_image_retrieve_view, name='product-image-retrieve-page'),
    path('product-image-update-page/<slug>/', product_image_update_view, name='product-image-update-page'),
    path('product-image-delete-page/<slug>/', product_image_delete_view, name='product-image-delete-page'),

]
