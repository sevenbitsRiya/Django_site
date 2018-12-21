from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', )

    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('popularity', 'popularity'),
        ('l2h', 'l2h'),
        ('h2l', 'h2l'),
    )
    filter_by = forms.ChoiceField(choices = FILTER_CHOICES)