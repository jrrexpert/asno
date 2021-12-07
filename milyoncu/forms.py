from django import forms

from  .models import Product, Cart

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price' , 'size' , 'category', 'logo')



class AddCart (forms.ModelForm):
    SIZE_CHOICES = [
    ('L', 'L'),
    ]

    quantity = forms.IntegerField(label='Quanitiy ', widget=forms.TextInput(attrs={"id":"quantity"}))
    size = forms.CharField(label='Size ', widget=forms.Select(attrs={"class":"selector"},choices=SIZE_CHOICES ))
    class Meta:
        model = Cart
        fields = ('size', 'quantity')
