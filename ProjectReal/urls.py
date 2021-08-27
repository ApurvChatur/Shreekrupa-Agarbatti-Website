from django.urls import path
from .views import home_view


app_name = 'ProjectReal'

urlpatterns = [
    path('', home_view, name='home-page')
]
