from django import forms
from .models import (Home,
                     Product,
                     ProductImage,
                     )


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__

