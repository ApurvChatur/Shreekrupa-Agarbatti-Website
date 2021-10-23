from django.contrib import admin
from .models import (Home,
                     Category,
                     Product,
                     )


admin.site.register(Home)
admin.site.register(Category)
admin.site.register(Product)
